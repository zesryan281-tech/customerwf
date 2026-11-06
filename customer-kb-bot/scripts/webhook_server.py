#!/usr/bin/env python3
"""
Customer Support Engine — Flask RAG engine + Kestra-facing API.

Two jobs in one process (optionally split later):

  A. Telegram front door
     POST /webhook/telegram   — Telegram Update JSON -> RAG -> reply

  B. Engine API, driven by Kestra HTTP tasks
     POST /engine/rag                     — answer a question (no side effects by default)
     POST /engine/notify                  — send a Telegram message (single delivery primitive)
     GET  /engine/customers               — list customers for a broadcast segment
     GET  /engine/customers/inactive      — customers not seen for N hours (follow-up driver)
     POST /engine/customers/touch         — mark contacted (resets the inactivity clock)
     GET  /engine/escalations             — inbound messages still unanswered after N minutes
     POST /engine/escalations/resolve     — close escalations
     GET  /engine/stats                   — counts, for health + flow summaries

  GET /health  — liveness + capability probe

Why this split: Kestra owns *when* (schedules, webhooks, retries, backoff,
concurrency, audit trail, alerting). Flask owns *what the answer is* (RAG over
the KB) and the Telegram transport.

Environment:
  TELEGRAM_BOT_TOKEN   (required)
  DATABASE_URL         (default: local socket pg)
  SUPPORT_CHAT_ID      (optional) target for /engine/notify with "to": "support"
  ENGINE_API_KEY       (optional) if set, /engine/* requires X-Engine-Key
  PORT                 (default 5000)
"""

import datetime
import json
import os
import re
import sys
import traceback

from flask import Flask, request, jsonify
import requests
import psycopg2
from psycopg2.extras import RealDictCursor

try:
    from sentence_transformers import SentenceTransformer
    _SENTENCE_TRANSFORMERS_AVAILABLE = True
except ImportError:
    SentenceTransformer = None
    _SENTENCE_TRANSFORMERS_AVAILABLE = False

# ---- Configuration ----
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not BOT_TOKEN:
    print("ERROR: TELEGRAM_BOT_TOKEN environment variable is required")
    sys.exit(1)

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://cndosks@localhost:5433/kb?host=/home/cndosks/.dsh/im/pg_socket&port=5433",
)

SUPPORT_CHAT_ID = (os.environ.get("SUPPORT_CHAT_ID") or "").strip()
ENGINE_API_KEY = (os.environ.get("ENGINE_API_KEY") or "").strip()

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

SEMANTIC_THRESHOLD = 0.30

# Ignored when keyword-matching FAQ questions; without this, "How do I reset my
# password?" matches any question containing "how", "you" or "does".
FAQ_STOPWORDS = {
    "the", "and", "for", "you", "your", "are", "can", "how", "does", "did",
    "what", "when", "where", "which", "who", "why", "with", "have", "has",
    "was", "were", "will", "would", "could", "should", "this", "that", "these",
    "those", "from", "into", "about", "there", "their", "them", "get", "got",
    "not", "but", "any", "all", "our", "out", "use", "using", "need", "want",
    "please", "help", "hello", "hi", "hey", "thanks", "thank", "take", "takes",
    "long", "much", "many", "some", "just", "know", "tell", "give", "make",
}

FALLBACK_REPLY = (
    "I'm not sure about that. Could you rephrase your question? "
    "You can ask about shipping, returns, password reset, or our products."
)

# ---- Flask app ----
app = Flask(__name__)

# ---- Lazy-loaded embedding model ----
_model = None


def get_model():
    """Load the embedding model if sentence-transformers is available."""
    global _model
    if _model is None:
        if not _SENTENCE_TRANSFORMERS_AVAILABLE:
            print("WARNING: sentence-transformers not installed; semantic search disabled.")
            return None
        print("Loading embedding model (all-MiniLM-L6-v2)...")
        _model = SentenceTransformer(EMBEDDING_MODEL_NAME)
        print("Embedding model loaded.")
    return _model


# ---- Database helpers ----

def get_db():
    return psycopg2.connect(DATABASE_URL)


def ensure_schema(conn):
    """
    Create the tables this engine needs. Idempotent, runs at startup so a fresh
    database works without a manual migration step.
    """
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS support_events (
            id               uuid PRIMARY KEY DEFAULT gen_random_uuid(),
            customer_id      uuid REFERENCES customers(id) ON DELETE SET NULL,
            channel          varchar(50) NOT NULL DEFAULT 'telegram',
            channel_user_id  text NOT NULL,
            question         text NOT NULL,
            answer           text,
            source           varchar(30),
            answered         boolean NOT NULL DEFAULT false,
            escalated_at     timestamptz,
            resolved_at      timestamptz,
            created_at       timestamptz NOT NULL DEFAULT now()
        )
        """
    )
    cur.execute(
        """
        CREATE INDEX IF NOT EXISTS support_events_open_idx
            ON support_events (created_at)
            WHERE resolved_at IS NULL
        """
    )
    cur.execute(
        """
        CREATE INDEX IF NOT EXISTS support_events_customer_idx
            ON support_events (channel, channel_user_id, created_at DESC)
        """
    )
    conn.commit()
    cur.close()


def vector_search_available(conn):
    """
    pgvector is optional. Probe it once so /engine/stats reports the truth and
    the semantic tier degrades instead of raising `operator does not exist`.
    """
    try:
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM pg_extension WHERE extname = 'vector'")
        if cur.fetchone() is None:
            cur.close()
            return False
        cur.execute(
            """
            SELECT data_type FROM information_schema.columns
            WHERE table_name = 'knowledge_chunks' AND column_name = 'embedding'
            """
        )
        row = cur.fetchone()
        cur.close()
        return bool(row) and row[0] in ("USER-DEFINED", "vector")
    except Exception:
        return False


# ---- Retrieval tiers ----

def search_faq(conn, user_text):
    """Keyword match over FAQ questions. Returns dict or None."""
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        words = [w for w in re.findall(r"[a-z0-9]+", user_text.lower())
                 if len(w) >= 3 and w not in FAQ_STOPWORDS]
        if not words:
            return None
        # Word-boundary match, not substring: "you" must not match "your".
        conditions = " OR ".join(["question ~* ('\\y' || %s || '\\y')"] * len(words))
        cur.execute(
            f"""
            SELECT question, answer, image_urls,
                   (SELECT count(*) FROM unnest(%s::text[]) AS w
                     WHERE question ~* ('\\y' || w || '\\y')) AS hits
            FROM faqs
            WHERE {conditions}
            ORDER BY hits DESC, length(question) ASC
            LIMIT 1
            """,
            [words] + words,
        )
        row = cur.fetchone()
    finally:
        cur.close()

    # Generic words ("how", "does", "take") can still graze an unrelated FAQ, so
    # require the FAQ question to cover at least half the meaningful words.
    if row and int(row["hits"]) >= max(1, (len(words) + 1) // 2):
        return {
            "answer": row["answer"],
            "title": row["question"],
            "images": list(row["image_urls"] or []),
            "source": "faq",
            "score": None,
        }
    return None


def search_content(conn, user_text):
    """Postgres full-text search over content_items. Returns dict or None."""
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        # OR the stemmed terms (plainto_tsquery ANDs them, so "shipping delivery
        # times" would match nothing; customers write multi-word questions).
        cur.execute(
            """
            WITH q AS (
                SELECT to_tsquery('english',
                           (SELECT string_agg(lexeme, ' | ')
                            FROM unnest(to_tsvector('english', %s)))) AS query
            )
            SELECT title, body_text, ts_rank(search_tsv, q.query) AS rank
            FROM content_items, q
            WHERE search_tsv @@ q.query
            ORDER BY rank DESC
            LIMIT 1
            """,
            (user_text,),
        )
        row = cur.fetchone()
    finally:
        cur.close()

    if row:
        return {
            "answer": row["body_text"],
            "title": row["title"],
            "images": [],
            "source": "content",
            "score": round(float(row["rank"]), 4),
        }
    return None


def search_semantic(conn, user_text, vector_ok):
    """pgvector cosine search. Returns dict or None when unavailable/no match."""
    if not vector_ok:
        return None
    model = get_model()
    if model is None:
        return None

    embedding = model.encode(user_text).tolist()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute(
            """
            SELECT kc.chunk_text, kc.source_type, ci.title,
                   1 - (kc.embedding <=> %s::vector) AS similarity
            FROM knowledge_chunks kc
            JOIN content_items ci ON ci.id = kc.content_id
            WHERE kc.embedding IS NOT NULL
              AND 1 - (kc.embedding <=> %s::vector) > %s
            ORDER BY kc.embedding <=> %s::vector
            LIMIT 3
            """,
            (embedding, embedding, SEMANTIC_THRESHOLD, embedding),
        )
        rows = cur.fetchall()
    finally:
        cur.close()

    if rows:
        best = rows[0]
        return {
            "answer": best["chunk_text"],
            "title": best["title"],
            "images": [],
            "source": "semantic",
            "score": round(float(best["similarity"]), 3),
        }
    return None


def answer_question(conn, question, vector_ok=None):
    """
    The RAG engine. FAQ -> full-text -> semantic -> fallback.
    Pure read: no Telegram calls, no writes. Safe for Kestra to call freely.
    """
    question = (question or "").strip()
    if not question:
        return {
            "found": False,
            "answer": FALLBACK_REPLY,
            "source": "fallback",
            "title": None,
            "images": [],
            "score": None,
        }

    if vector_ok is None:
        vector_ok = vector_search_available(conn)

    for hit in (
        search_faq(conn, question),
        search_content(conn, question),
        search_semantic(conn, question, vector_ok),
    ):
        if hit:
            hit["found"] = True
            return hit

    return {
        "found": False,
        "answer": FALLBACK_REPLY,
        "source": "fallback",
        "title": None,
        "images": [],
        "score": None,
    }


# ---- Customer / event persistence ----

def upsert_customer(conn, channel_user_id, name=""):
    """Upsert a customer and return its id."""
    cur = conn.cursor()
    try:
        cur.execute(
            """
            INSERT INTO customers (id, name, channel, channel_user_id, preferences, last_seen)
            VALUES (gen_random_uuid(), %s, 'telegram', %s, '{}'::jsonb, now())
            ON CONFLICT (channel, channel_user_id)
            DO UPDATE SET last_seen = now(),
                          name = COALESCE(NULLIF(EXCLUDED.name, ''), customers.name)
            RETURNING id
            """,
            (name, str(channel_user_id)),
        )
        customer_id = cur.fetchone()[0]
        conn.commit()
        return customer_id
    finally:
        cur.close()


def log_support_event(conn, customer_id, channel_user_id, question, result, answered=True):
    """Record an inbound question and the answer the engine produced."""
    cur = conn.cursor()
    try:
        cur.execute(
            """
            INSERT INTO support_events
                (customer_id, channel, channel_user_id, question, answer, source, answered)
            VALUES (%s, 'telegram', %s, %s, %s, %s, %s)
            """,
            (
                customer_id,
                str(channel_user_id),
                question,
                result.get("answer"),
                result.get("source"),
                answered,
            ),
        )
        conn.commit()
    finally:
        cur.close()


# ---- Telegram helpers ----

def telegram_send_message(chat_id, text, parse_mode=None):
    url = f"{TELEGRAM_API}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "disable_web_page_preview": True,
    }
    if parse_mode:
        payload["parse_mode"] = parse_mode
    r = requests.post(url, json=payload, timeout=15)
    data = r.json() if r.content else {}
    if not r.ok or not data.get("ok"):
        raise RuntimeError(f"telegram sendMessage failed: {r.status_code} {data}")
    return data


def telegram_send_photo(chat_id, photo_url, caption=None):
    url = f"{TELEGRAM_API}/sendPhoto"
    payload = {"chat_id": chat_id, "photo": photo_url}
    if caption:
        payload["caption"] = caption
    r = requests.post(url, json=payload, timeout=15)
    return r.json() if r.content else {}


# ---- Engine API auth ----

@app.before_request
def _engine_auth():
    if not ENGINE_API_KEY:
        return None
    if not request.path.startswith("/engine/"):
        return None
    if request.headers.get("X-Engine-Key") == ENGINE_API_KEY:
        return None
    return jsonify({"ok": False, "error": "missing or invalid X-Engine-Key"}), 401


# =====================================================================
# A. Telegram front door
# =====================================================================

@app.route("/webhook/telegram", methods=["POST"])
def telegram_webhook():
    try:
        update = request.get_json(force=True)
    except Exception:
        return jsonify({"ok": False, "error": "invalid JSON"}), 400

    message = update.get("message") or update.get("edited_message")
    if not message:
        return jsonify({"ok": True})

    chat = message.get("chat", {})
    chat_id = chat.get("id")
    user_text = (message.get("text") or "").strip()

    if not chat_id or not user_text:
        return jsonify({"ok": True})

    result = dict(found=False, answer=FALLBACK_REPLY, source="fallback",
                  title=None, images=[], score=None)

    try:
        conn = get_db()
        customer_id = upsert_customer(conn, chat_id, chat.get("first_name", ""))
        result = answer_question(conn, user_text)
        log_support_event(conn, customer_id, chat_id, user_text, result, answered=True)
        conn.close()
    except Exception as e:
        print(f"KB search error: {e}")
        traceback.print_exc()
        result = dict(found=False,
                      answer="Sorry, I'm having trouble accessing the knowledge base right now.",
                      source="error", title=None, images=[], score=None)

    try:
        telegram_send_message(chat_id, result["answer"])
        for img_url in (result.get("images") or [])[:3]:
            telegram_send_photo(chat_id, img_url)
    except Exception as e:
        print(f"telegram delivery error: {e}")

    return jsonify({"ok": True, "source": result.get("source")})


# =====================================================================
# B. Engine API — called by Kestra HTTP tasks
# =====================================================================

@app.route("/engine/rag", methods=["POST"])
def engine_rag():
    """
    Body: {"question": str, "record": bool=false,
           "channel_user_id": str?, "name": str?}
    Pure RAG lookup. With record=true it also upserts the customer and logs the
    event, which is what a Kestra-fronted webhook flow needs.
    """
    body = request.get_json(silent=True) or {}
    question = body.get("question") or ""
    if not question.strip():
        return jsonify({"ok": False, "error": "question is required"}), 400

    conn = get_db()
    try:
        result = answer_question(conn, question)
        if body.get("record"):
            cid = body.get("channel_user_id")
            if not cid:
                return jsonify({"ok": False,
                                "error": "channel_user_id is required when record=true"}), 400
            customer_id = upsert_customer(conn, cid, body.get("name", ""))
            log_support_event(conn, customer_id, cid, question, result, answered=True)
        return jsonify({"ok": True, **result})
    except Exception as e:
        traceback.print_exc()
        return jsonify({"ok": False, "error": str(e)}), 500
    finally:
        conn.close()


@app.route("/engine/notify", methods=["POST"])
def engine_notify():
    """
    Body: {"channel_user_id": str} or {"to": "support"},
          {"text": str, "parse_mode": str?, "images": [url]?}
    The only delivery primitive Kestra needs.
    """
    body = request.get_json(silent=True) or {}
    text = body.get("text") or ""
    target = body.get("channel_user_id") or (SUPPORT_CHAT_ID if body.get("to") == "support" else None)

    if not text.strip():
        return jsonify({"ok": False, "error": "text is required"}), 400
    if not target:
        return jsonify({"ok": False,
                        "error": "channel_user_id is required (or to='support' with SUPPORT_CHAT_ID set)"}), 400

    try:
        sent = telegram_send_message(target, text, body.get("parse_mode"))
        ids = [sent.get("result", {}).get("message_id")]
        for img in (body.get("images") or [])[:3]:
            telegram_send_photo(target, img)
        return jsonify({"ok": True, "chat_id": target, "message_ids": ids})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 502


@app.route("/engine/customers", methods=["GET"])
def engine_customers():
    """?segment=all|inactive_7d&limit=200 — recipients for a broadcast."""
    segment = request.args.get("segment", "all")
    limit = max(1, min(int(request.args.get("limit", 200)), 1000))
    where = "channel_user_id IS NOT NULL"
    if segment == "inactive_7d":
        where += " AND (last_seen IS NULL OR last_seen < now() - interval '7 days')"

    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute(
            f"""
            SELECT channel_user_id, name, last_seen
            FROM customers
            WHERE {where}
            ORDER BY last_seen DESC NULLS LAST
            LIMIT %s
            """,
            (limit,),
        )
        rows = cur.fetchall()
    finally:
        cur.close()
        conn.close()

    return jsonify({
        "ok": True,
        "segment": segment,
        "count": len(rows),
        "customers": [
            {
                "channel_user_id": r["channel_user_id"],
                "name": r["name"],
                "last_seen": r["last_seen"].isoformat() if r["last_seen"] else None,
            }
            for r in rows
        ],
    })


@app.route("/engine/customers/inactive", methods=["GET"])
def engine_customers_inactive():
    """?hours=72&limit=50 — drives the follow-up flow."""
    hours = max(1, int(request.args.get("hours", 72)))
    limit = max(1, min(int(request.args.get("limit", 50)), 500))

    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute(
            """
            SELECT channel_user_id, name, last_seen,
                   EXTRACT(EPOCH FROM (now() - last_seen)) / 3600 AS hours_since,
                   COALESCE((preferences->>'followups')::int, 0) AS followups
            FROM customers
            WHERE channel_user_id IS NOT NULL
              AND (last_seen IS NULL OR last_seen < now() - make_interval(hours => %s))
            ORDER BY last_seen ASC NULLS FIRST
            LIMIT %s
            """,
            (hours, limit),
        )
        rows = cur.fetchall()
    finally:
        cur.close()
        conn.close()

    return jsonify({
        "ok": True,
        "hours": hours,
        "count": len(rows),
        "customers": [
            {
                "channel_user_id": r["channel_user_id"],
                "name": r["name"],
                "last_seen": r["last_seen"].isoformat() if r["last_seen"] else None,
                "hours_since": round(float(r["hours_since"]), 1) if r["hours_since"] is not None else None,
                "followups_sent": int(r["followups"]),
            }
            for r in rows
        ],
    })


@app.route("/engine/customers/touch", methods=["POST"])
def engine_customers_touch():
    """Body: {"channel_user_id": str} — mark contacted, reset the inactivity clock."""
    body = request.get_json(silent=True) or {}
    cid = body.get("channel_user_id")
    if not cid:
        return jsonify({"ok": False, "error": "channel_user_id is required"}), 400

    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute(
            """
            UPDATE customers
            SET last_seen = now(),
                preferences = COALESCE(preferences, '{}'::jsonb) || jsonb_build_object(
                    'followups', COALESCE((preferences->>'followups')::int, 0) + 1,
                    'last_followup_at', now()::text
                )
            WHERE channel_user_id = %s
            RETURNING id
            """,
            (str(cid),),
        )
        row = cur.fetchone()
        conn.commit()
    finally:
        cur.close()
        conn.close()

    if not row:
        return jsonify({"ok": False, "error": f"unknown customer {cid}"}), 404
    return jsonify({"ok": True, "channel_user_id": str(cid)})


@app.route("/engine/escalations", methods=["GET"])
def engine_escalations():
    """?minutes=60&limit=20 — inbound messages still unresolved after N minutes."""
    minutes = max(1, int(request.args.get("minutes", 60)))
    limit = max(1, min(int(request.args.get("limit", 20)), 200))

    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute(
            """
            SELECT se.id, se.channel_user_id, c.name, se.question, se.answer, se.source,
                   se.created_at,
                   EXTRACT(EPOCH FROM (now() - se.created_at)) / 60 AS minutes_waiting
            FROM support_events se
            LEFT JOIN customers c ON c.id = se.customer_id
            WHERE se.resolved_at IS NULL
              AND se.created_at < now() - make_interval(mins => %s)
            ORDER BY se.created_at ASC
            LIMIT %s
            """,
            (minutes, limit),
        )
        rows = cur.fetchall()
    finally:
        cur.close()
        conn.close()

    return jsonify({
        "ok": True,
        "minutes": minutes,
        "count": len(rows),
        "escalations": [
            {
                "id": str(r["id"]),
                "channel_user_id": r["channel_user_id"],
                "name": r["name"],
                "question": r["question"],
                "answer": r["answer"],
                "source": r["source"],
                "created_at": r["created_at"].isoformat(),
                "minutes_waiting": round(float(r["minutes_waiting"]), 1),
            }
            for r in rows
        ],
    })


@app.route("/engine/escalations/resolve", methods=["POST"])
def engine_escalations_resolve():
    """Body: {"ids": [uuid]} or {"channel_user_id": str} — close escalations."""
    body = request.get_json(silent=True) or {}
    ids = body.get("ids") or []
    cid = body.get("channel_user_id")
    if not ids and not cid:
        return jsonify({"ok": False, "error": "ids or channel_user_id is required"}), 400

    conn = get_db()
    cur = conn.cursor()
    try:
        if ids:
            cur.execute(
                """
                UPDATE support_events SET resolved_at = now()
                WHERE id = ANY(%s::uuid[]) AND resolved_at IS NULL
                """,
                (ids,),
            )
        else:
            cur.execute(
                """
                UPDATE support_events SET resolved_at = now()
                WHERE channel_user_id = %s AND resolved_at IS NULL
                """,
                (str(cid),),
            )
        n = cur.rowcount
        conn.commit()
    finally:
        cur.close()
        conn.close()

    return jsonify({"ok": True, "resolved": n})


@app.route("/engine/stats", methods=["GET"])
def engine_stats():
    conn = get_db()
    try:
        vector_ok = vector_search_available(conn)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        try:
            cur.execute(
                """
                SELECT
                  (SELECT count(*) FROM faqs)             AS faqs,
                  (SELECT count(*) FROM content_items)    AS content_items,
                  (SELECT count(*) FROM knowledge_chunks) AS knowledge_chunks,
                  (SELECT count(*) FROM customers)        AS customers,
                  (SELECT count(*) FROM support_events)   AS support_events,
                  (SELECT count(*) FROM support_events
                    WHERE resolved_at IS NULL)            AS open_events
                """
            )
            counts = dict(cur.fetchone())
        finally:
            cur.close()
    finally:
        conn.close()

    return jsonify({
        "ok": True,
        "counts": counts,
        "capabilities": {
            "faq_exact": True,
            "full_text": True,
            "semantic_vector": bool(vector_ok and _SENTENCE_TRANSFORMERS_AVAILABLE),
            "pgvector_installed": bool(vector_ok),
            "embedding_model_installed": _SENTENCE_TRANSFORMERS_AVAILABLE,
            "telegram_delivery": True,
            "support_chat_configured": bool(SUPPORT_CHAT_ID),
        },
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "bot": BOT_TOKEN[:8] + "...", "engine_api": True})


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "service": "Customer KB Bot — Flask RAG engine for Kestra",
        "endpoints": {
            "POST /webhook/telegram": "Telegram webhook receiver (RAG + reply)",
            "POST /engine/rag": "Answer a question (Kestra HTTP task)",
            "POST /engine/notify": "Send a Telegram message (Kestra HTTP task)",
            "GET  /engine/customers": "Broadcast recipients",
            "GET  /engine/customers/inactive": "Follow-up candidates",
            "POST /engine/customers/touch": "Mark contacted",
            "GET  /engine/escalations": "Unresolved inbound messages",
            "POST /engine/escalations/resolve": "Close escalations",
            "GET  /engine/stats": "Counts + capabilities",
            "GET  /health": "Health check",
        },
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting support engine on port {port}")
    print(f"Bot token: {BOT_TOKEN[:8]}...")
    print(f"Database: {DATABASE_URL}")
    print(f"Support chat: {SUPPORT_CHAT_ID or '(not set)'}")
    print(f"Engine API key: {'set' if ENGINE_API_KEY else '(open)'}")
    try:
        _c = get_db()
        ensure_schema(_c)
        print(f"support_events ready; pgvector={vector_search_available(_c)}")
        _c.close()
    except Exception as _e:
        print(f"WARNING: schema bootstrap failed: {_e}")
    app.run(host="0.0.0.0", port=port, debug=False)
