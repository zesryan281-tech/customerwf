# Customer KB Bot — Workflow: Start, Repair, Fix, Update

## Project Overview

- **Bot:** `@spdhdod_bot` (token: `8790668279:AAEVKmp-87yWTCGtWr2C-L3K2fxxUiw03ig`)
- **Webhook server:** Flask on port 5000
- **Database:** PostgreSQL 18 on port 5433 (socket dir: `/home/cndosks/.dsh/im/pg_socket`)
- **Public tunnel:** Cloudflare Tunnel (trycloudflare.com URL — changes on restart)
- **Workspace root:** `/home/cndosks/.dsh/im`

---

## File & Folder Layout

```
/home/cndosks/.dsh/im/
├── WORKFLOW.md                  # This file — start / repair / fix / update guide
├── setup_all.sh                 # One-shot setup script (DB + webhook + Cloudflare)
├── pgdata/                      # PostgreSQL 18 data directory
├── pg_socket/                   # PostgreSQL Unix socket directory
├── pg.log                       # PostgreSQL log
├── cloudflared                  # Cloudflare Tunnel binary
├── cloudflared.log              # Cloudflare Tunnel log (contains the public URL)
├── webhook_server.log           # Flask webhook server log
├── .venv/                       # Python virtual environment
├── customer-kb-bot/
│   ├── README.md                # Project overview
│   ├── db/
│   │   └── schema.sql           # PostgreSQL schema (6 tables + pgvector)
│   ├── scripts/
│   │   ├── webhook_server.py    # Flask webhook server + RAG search
│   │   └── ingest.py            # JSON → DB ingestion script
│   ├── content/
│   │   └── content.json         # Your FAQs, policies, products (+ images)
│   └── research/
│       └── channel-research.md  # WeChat / Facebook channel setup guide
└── research/
    └── channel-research.md
```

---

## 1. HOW TO START (Full Boot)

All three components must be running: **PostgreSQL → Webhook Server → Cloudflare Tunnel → Telegram Webhook**.

### Step 1: Start PostgreSQL

```bash
cd /home/cndosks/.dsh/im

/usr/lib/postgresql/18/bin/pg_ctl -D pgdata \
  -o "-p 5433 -c unix_socket_directories='pg_socket'" \
  -l pg.log start -w

sleep 1

# Verify it's running
export PGHOST=/home/cndosks/.dsh/im/pg_socket PGPORT=5433 PGDATABASE=kb PGUSER=cndosks
psql -c "SELECT count(*) FROM content_items;"
```

Expected: a row count (e.g., `3`).

### Step 2: Start the Webhook Server

```bash
cd /home/cndosks/.dsh/im/customer-kb-bot

export TELEGRAM_BOT_TOKEN="8790668279:AAEVKmp-87yWTCGtWr2C-L3K2fxxUiw03ig"
export DATABASE_URL="postgresql://cndosks@localhost:5433/kb?host=/home/cndosks/.dsh/im/pg_socket&port=5433"
export PORT=5000

nohup /home/cndosks/.dsh/im/.venv/bin/python scripts/webhook_server.py \
  > /home/cndosks/.dsh/im/webhook_server.log 2>&1 &

sleep 3
curl http://127.0.0.1:5000/health
```

Expected: `{"bot":"87906682...","status":"ok"}`

### Step 3: Start Cloudflare Tunnel

```bash
cd /home/cndosks/.dsh/im

nohup ./cloudflared tunnel --url http://127.0.0.1:5000 \
  > cloudflared.log 2>&1 &

sleep 10

# Extract the public URL
grep -o 'https://[a-zA-Z0-9.-]*\.trycloudflare\.com' cloudflared.log | head -1
```

Expected: a URL like `https://xxxx-xxxx-xxxx.trycloudflare.com`

> **⚠️ trycloudflare.com URLs are temporary.** Each restart gives a new URL. You must re-run Step 4 after each tunnel restart.

### Step 4: Set the Telegram Webhook

```bash
cd /home/cndosks/.dsh/im

CF_URL="https://waiting-brad-hydrocodone-laboratories.trycloudflare.com"  # <- from Step 3
BOT_TOKEN="8790668279:AAEVKmp-87yWTCGtWr2C-L3K2fxxUiw03ig"

curl -s -X POST "https://api.telegram.org/bot${BOT_TOKEN}/setWebhook" \
  -H "Content-Type: application/json" \
  -d "{\"url\":\"${CF_URL}/webhook/telegram\"}"

# Verify
curl -s "https://api.telegram.org/bot${BOT_TOKEN}/getWebhookInfo"
```

Expected: `{"ok":true,"result":{"url":"...","pending_update_count":0,...}}`

### Step 5: Test End-to-End

Message **@spdhdod_bot** on Telegram with: `How do I reset my password?`

You should get a reply from the bot.

---

## 2. ONE-COMMAND FULL STARTUP

If everything is stopped, run `setup_all.sh`:

```bash
cd /home/cndosks/.dsh/im
chmod +x setup_all.sh
./setup_all.sh
```

This does all 4 steps above in order. Check the output for the Cloudflare URL and webhook confirmation.

---

## 3. HOW TO REPAIR (Common Issues)

### Issue A: Webhook server not responding (port 5000 dead)

**Symptoms:** `curl http://127.0.0.1:5000/health` fails or connection refused.

**Fix:**
```bash
# Kill anything on port 5000
pkill -f webhook_server 2>/dev/null || true

# Restart
cd /home/cndosks/.dsh/im/customer-kb-bot
export TELEGRAM_BOT_TOKEN="8790668279:AAEVKmp-87yWTCGtWr2C-L3K2fxxUiw03ig"
export DATABASE_URL="postgresql://cndosks@localhost:5433/kb?host=/home/cndosks/.dsh/im/pg_socket&port=5433"
export PORT=5000
nohup /home/cndosks/.dsh/im/.venv/bin/python scripts/webhook_server.py \
  > /home/cndosks/.dsh/im/webhook_server.log 2>&1 &
sleep 3
curl http://127.0.0.1:5000/health
```

Then restart Cloudflare Tunnel and re-set the webhook (Steps 3–4 above).

### Issue B: PostgreSQL not running

**Symptoms:** `psql` fails, `connection refused on socket`.

**Fix:**
```bash
cd /home/cndosks/.dsh/im

# Check if postmaster is running
pg_ctl -D pgdata status

# If not running, start it
/usr/lib/postgresql/18/bin/pg_ctl -D pgdata \
  -o "-p 5433 -c unix_socket_directories='pg_socket'" \
  -l pg.log start -w

# If it crashed, check the log
tail -20 pg.log
```

### Issue C: Cloudflare Tunnel URL changed (bot not responding on Telegram)

**Symptoms:** You message the bot but get no reply. Cloudflare URL is different from what's set in Telegram.

**Fix:** Get the new URL and re-set the webhook:
```bash
cd /home/cndosks/.dsh/im
CF_URL=$(grep -o 'https://[a-zA-Z0-9.-]*\.trycloudflare\.com' cloudflared.log | head -1)
BOT_TOKEN="8790668279:AAEVKmp-87yWTCGtWr2C-L3K2fxxUiw03ig"
curl -s -X POST "https://api.telegram.org/bot${BOT_TOKEN}/setWebhook" \
  -H "Content-Type: application/json" \
  -d "{\"url\":\"${CF_URL}/webhook/telegram\"}"
```

### Issue D: Full-text search error (`column "search_tsv" does not exist`)

**Symptoms:** Webhook server log shows `column "search_tsv" does not exist`.

**Fix:**
```bash
cd /home/cndosks/.dsh/im
export PGHOST=/home/cndosks/.dsh/im/pg_socket PGPORT=5433 PGDATABASE=kb PGUSER=cndosks

psql -c "
ALTER TABLE content_items ADD COLUMN IF NOT EXISTS search_tsv TSVECTOR
  GENERATED ALWAYS AS (
    to_tsvector('english', coalesce(title, '') || ' ' || coalesce(body_text, ''))
  ) STORED;
CREATE INDEX IF NOT EXISTS idx_content_items_search_tsv ON content_items USING gin (search_tsv);
"
```

### Issue E: pgvector not installed (semantic search disabled)

**Symptoms:** `knowledge_chunks.embedding` column is `text` instead of `vector(384)`. Semantic search falls back silently.

**Fix:** pgvector requires root/install privileges. Without it, semantic search is disabled but FAQ + full-text search still work. To enable later, install the `postgresql-18-pgvector` package and re-create the schema with `CREATE EXTENSION vector;`.

---

## 4. HOW TO FIX (Troubleshooting Checklist)

| Symptom | First thing to check | Command |
|---------|---------------------|---------|
| Bot doesn't reply | Is webhook server running? | `curl http://127.0.0.1:5000/health` |
| Webhook server crashes | Check the log | `cat /home/cndosks/.dsh/im/webhook_server.log` |
| Cloudflare tunnel down | Is cloudflared running? | `ps aux \| grep cloudflared` |
| Wrong public URL | Check cloudflared.log | `grep trycloudflare /home/cndosks/.dsh/im/cloudflared.log` |
| Telegram webhook wrong URL | Check Telegram | `curl https://api.telegram.org/bot<TOKEN>/getWebhookInfo` |
| DB search errors | Check PostgreSQL log | `tail /home/cndosks/.dsh/im/pg.log` |
| Content not found | Check data in DB | `psql ... -c "SELECT * FROM faqs;"` |

### Quick Health Check (run all)

```bash
cd /home/cndosks/.dsh/im

echo "=== PostgreSQL ==="
export PGHOST=/home/cndosks/.dsh/im/pg_socket PGPORT=5433 PGDATABASE=kb PGUSER=cndosks
psql -c "SELECT count(*) FROM content_items;"

echo "=== Webhook Server ==="
curl -s http://127.0.0.1:5000/health

echo "=== Cloudflare Tunnel ==="
grep -o 'https://[a-zA-Z0-9.-]*\.trycloudflare\.com' cloudflared.log | head -1

echo "=== Telegram Webhook ==="
BOT_TOKEN="8790668279:AAEVKmp-87yWTCGtWr2C-L3K2fxxUiw03ig"
curl -s "https://api.telegram.org/bot${BOT_TOKEN}/getWebhookInfo" | head -c 300
```

---

## 5. HOW TO UPDATE

### Update Content (FAQs, policies, products, images)

Edit `/home/cndosks/.dsh/im/customer-kb-bot/content/content.json`, then re-ingest:

```bash
cd /home/cndosks/.dsh/im/customer-kb-bot

export PGHOST=/home/cndosks/.dsh/im/pg_socket PGPORT=5433 PGDATABASE=kb PGUSER=cndosks
DATABASE_URL="postgresql://cndosks@localhost:5433/kb?host=/home/cndosks/.dsh/im/pg_socket&port=5433"

/home/cndosks/.dsh/im/.venv/bin/python scripts/ingest.py \
  --file content/content.json \
  --db "$DATABASE_URL"
```

> **Note:** `ingest.py` requires `sentence-transformers` (not currently installed). If it fails, install it first or manually insert content via SQL.

### Add a New FAQ Manually

```sql
INSERT INTO faqs (question, answer) VALUES
('Your question here', 'Your answer here');
```

### Add New Content Item

```sql
INSERT INTO content_items (title, body_text, category, status) VALUES
('New Title', 'New body text', 'policy', 'published');
```

### Update the Webhook Server Code

Edit `/home/cndosks/.dsh/im/customer-kb-bot/scripts/webhook_server.py`, then restart the webhook server:

```bash
pkill -f webhook_server 2>/dev/null || true
cd /home/cndosks/.dsh/im/customer-kb-bot
export TELEGRAM_BOT_TOKEN="8790668279:AAEVKmp-87yWTCGtWr2C-L3K2fxxUiw03ig"
export DATABASE_URL="postgresql://cndosks@localhost:5433/kb?host=/home/cndosks/.dsh/im/pg_socket&port=5433"
export PORT=5000
nohup /home/cndosks/.dsh/im/.venv/bin/python scripts/webhook_server.py \
  > /home/cndosks/.dsh/im/webhook_server.log 2>&1 &
```

### Update Database Schema

Edit `/home/cndosks/.dsh/im/customer-kb-bot/db/schema.sql`, then apply changes:

```bash
cd /home/cndosks/.dsh/im
export PGHOST=/home/cndosks/.dsh/im/pg_socket PGPORT=5433 PGDATABASE=kb PGUSER=cndosks
psql -f customer-kb-bot/db/schema.sql
```

> **Warning:** Running `schema.sql` on an existing database will fail on `CREATE TABLE IF NOT EXISTS` is not used — tables already exist. Use `ALTER TABLE` for additions instead.

### Add pgvector (Enable Semantic Search)

Requires root access to install the package:

```bash
# Needs root — run on host if you have sudo
sudo dpkg -i /home/cndosks/.dsh/im/postgresql-18-pgvector_0.8.1-2_amd64.deb

# Then in the database:
export PGHOST=/home/cndosks/.dsh/im/pg_socket PGPORT=5433 PGDATABASE=kb PGUSER=cndosks
psql -c "CREATE EXTENSION IF NOT EXISTS vector;"
psql -c "ALTER TABLE knowledge_chunks ALTER COLUMN embedding TYPE vector(384);"
```

Then re-run `ingest.py` (which requires `sentence-transformers`) to generate embeddings.

---

## 6. STOP / SHUTDOWN

```bash
# Stop webhook server
pkill -f webhook_server 2>/dev/null || true

# Stop Cloudflare Tunnel
pkill -f cloudflared 2>/dev/null || true

# Stop PostgreSQL
/usr/lib/postgresql/18/bin/pg_ctl -D /home/cndosks/.dsh/im/pgdata stop
```

---

## 7. KEY FILES SUMMARY

| File | Purpose |
|------|---------|
| `setup_all.sh` | One-shot full setup script |
| `customer-kb-bot/scripts/webhook_server.py` | Flask webhook + RAG search + Telegram replies |
| `customer-kb-bot/scripts/ingest.py` | JSON content → PostgreSQL ingestion |
| `customer-kb-bot/db/schema.sql` | Database schema (6 tables) |
| `customer-kb-bot/content/content.json` | Your FAQs, policies, products (edit this) |
| `customer-kb-bot/research/channel-research.md` | WeChat / Facebook channel guides |
| `pgdata/` | PostgreSQL data (do not edit manually) |
| `cloudflared.log` | Contains current public tunnel URL |
| `webhook_server.log` | Flask server logs (check for errors) |
| `pg.log` | PostgreSQL logs |

---

## 8. QUICK REFERENCE COMMANDS

```bash
# Start everything
./setup_all.sh

# Check webhook health
curl http://127.0.0.1:5000/health

# Get current Cloudflare URL
grep -o 'https://[a-zA-Z0-9.-]*\.trycloudflare\.com' cloudflared.log | head -1

# Re-set Telegram webhook
curl -s -X POST "https://api.telegram.org/bot8790668279:AAEVKmp-87yWTCGtWr2C-L3K2fxxUiw03ig/setWebhook" \
  -H "Content-Type: application/json" -d "{\"url\":\"https://YOUR-URL/webhook/telegram\"}"

# Check Telegram webhook status
curl -s "https://api.telegram.org/bot8790668279:AAEVKmp-87yWTCGtWr2C-L3K2fxxUiw03ig/getWebhookInfo"

# Query database
psql -h /home/cndosks/.dsh/im/pg_socket -p 5433 -U cndosks -d kb -c "SELECT * FROM faqs;"

# View webhook logs
tail -50 webhook_server.log

# View Cloudflare logs
tail -50 cloudflared.log
```

---

**Your bot is live at:** Message `@spdhdod_bot` on Telegram.

---

## Part 2 — Hybrid Mode: Kestra Orchestration (Option C, active since 2026-10-22)

Kestra (127.0.0.1:8080) is the orchestrator; the Flask RAG engine runs as Docker
container `support-engine` (image `support-engine:local`) on the Kestra network.
Telegram messages hit **Kestra's webhook first**, Kestra calls the engine over
the Docker network, and the engine owns all Telegram delivery (it holds the bot
token — Kestra secrets are read-only and can't store it).

### Architecture

```
Telegram ──> Cloudflare tunnel ──> Kestra webhook (customer-auto-reply)
                                        │
                                        ▼  (HTTP tasks, Docker DNS)
                                 support-engine:5000  (Flask RAG)
                                   /engine/rag  /engine/notify
                                        │
                                        ▼
                                 host PostgreSQL (kb @ /pg_socket)
```

### The 4 flows (namespace `customer-support`, files in customer-kb-bot/kestra/flows/)

| Flow | Trigger | What it does |
|---|---|---|
| `customer-auto-reply` | Webhook key `telegram-reply` | Front door: text message → `/engine/rag` (records customer + event) → `/engine/notify` (reply + up to 3 images) |
| `followup-inactive` | Schedule `0 * * * *` (hourly) | Customers inactive ≥ 72h get a follow-up, then `/engine/customers/touch` so they aren't re-notified |
| `escalation-digest` | Schedule `30 * * * *` | Events unresolved for > 60 min → digest to support chat (`SUPPORT_CHAT_ID` on the engine container) |
| `broadcast` | Manual only | Sends one message to every customer (input: `message`) |

Deploy: `cd customer-kb-bot/kestra && ./deploy.sh flows/<file>.yaml` (deploys all flows/ if no arg).

### Startup order (after a host reboot)

1. **PostgreSQL** (persistent terminal — bash tool calls die with bwrap):
   `/usr/lib/postgresql/18/bin/pg_ctl -D /home/cndosks/.dsh/im/pgdata -o "-p 5433 -c unix_socket_directories=/home/cndosks/.dsh/im/pg_socket -c listen_addresses=127.0.0.1" -l /home/cndosks/.dsh/im/pg.log start -w`
2. **Engine container**: see `docker inspect support-engine` for the exact run line; needs `-e SUPPORT_CHAT_ID=6009345177`, `-v /home/cndosks/.dsh/im/pg_socket:/pg_socket`, network `kestra-facebook_kestra-network`, `-p 5000:5000`.
3. **Kestra + kestra-postgres containers**: `docker start kestra-postgres kestra`.
4. **Cloudflared** (persistent terminal): `nohup /home/cndosks/.dsh/im/cloudflared tunnel --url http://127.0.0.1:8080 > /home/cndosks/.dsh/im/cloudflared.log 2>&1 &`
5. **Re-register the Telegram webhook** (trycloudflare URLs are EPHEMERAL — new URL every restart):
   ```bash
   URL=$(grep -o 'https://[a-z0-9-]*\.trycloudflare\.com' cloudflared.log | head -1)
   curl -s "https://api.telegram.org/bot8790668279:AAEVKmp-87yWTCGtWr2C-L3K2fxxUiw03ig/setWebhook" \
     -X POST -H 'Content-Type: application/json' \
     -d "{\"url\":\"$URL/api/v1/executions/webhook/customer-support/customer-auto-reply/telegram-reply\"}"
   ```

### Ops cheatsheet

```bash
# Trigger flows manually (basic auth: aiizxcvbnm9911@gmail.com / Zxcvbnm123@)
curl -s -u "aiizxcvbnm9911@gmail.com:Zxcvbnm123@" -X POST "http://127.0.0.1:8080/api/v1/main/executions/customer-support/escalation-digest?wait=true"
# With inputs (multipart, NOT JSON — 415 otherwise):
curl -s -u "aiizxcvbnm9911@gmail.com:Zxcvbnm123@" -X POST "http://127.0.0.1:8080/api/v1/main/executions/customer-support/broadcast?wait=true" -F "message=Hello!"
curl -s -u "aiizxcvbnm9911@gmail.com:Zxcvbnm123@" -X POST "http://127.0.0.1:8080/api/v1/main/executions/customer-support/followup-inactive?wait=true" -F "hours=24"

# Resolve escalations after handling them
curl -s -X POST http://127.0.0.1:5000/engine/escalations/resolve -H 'Content-Type: application/json' -d '{"channel_user_id":"6009345177"}'

# Engine status / Kestra executions
curl -s http://127.0.0.1:5000/engine/stats
curl -s -u "aiizxcvbnm9911@gmail.com:Zxcvbnm123@" "http://127.0.0.1:8080/api/v1/main/executions/search?namespace=customer-support&flowId=customer-auto-reply&size=5"
```

### Kestra 2.0.3 gotchas (empirically verified on THIS instance)

- JSON serialization filter is **`| toJson`** — `| json`, `json()`, `| jsonEncode` do NOT exist.
- Webhook `trigger.body` is a **parsed object** (use `trigger.body.message.text` directly, NOT `json(trigger.body)`).
- Webhook endpoints are **public** (no basic auth) — Telegram can POST directly.
- Loop iteration variable is **`item.value`** (`fromJson(item.value).field`); `taskrun.value` does NOT exist in child tasks. Loop `values:` takes `{{ [...] | toJson }}`.
- `{{ x.y ?? 'default' }}` null-safe chains work and do not throw on missing keys.
- Flow inputs: `defaults:`; manual executions with inputs need `multipart/form-data` (JSON body → HTTP 415).
- `minutes` on `/engine/escalations` is a MINIMUM AGE (`created_at < now() - N minutes`), not a lookback window.
- Engine `/engine/notify` returns **502** on Telegram failure → pair loop send-tasks with `allowFailure: true` (one bad chat id must not kill a broadcast).
- `/tmp` does not persist between agent bash calls (bwrap) — keep temp files in the workspace.

### Known limitations

- Semantic tier OFF: pgvector not installed on host PG (`postgresql-18-pgvector_0.8.1-2_amd64.deb` exists but uninstalled) and no embedding model in the engine image → RAG = FAQ exact match + full-text.
- trycloudflare.com tunnels are ephemeral; a restart changes the URL, so re-run setWebhook (step 5) after every cloudflared restart.
- Kestra secrets are read-only (env backend) — the bot token lives only on the engine container.
