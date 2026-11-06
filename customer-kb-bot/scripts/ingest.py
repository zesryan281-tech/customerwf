#!/usr/bin/env python3
"""
Starter ingestion script for the Customer Knowledge Base.

Reads content from a JSON file and inserts it into PostgreSQL:
  - content_items (text articles, FAQs, policies)
  - content_images (image URLs + thumbnails)
  - knowledge_chunks with embeddings (for RAG semantic search)

Usage:
    python ingest.py --file content.json --db "postgresql://user:pass@localhost:5432/kb"
"""

import argparse
import hashlib
import json
import os
import sys
import uuid

try:
    import psycopg2
    from psycopg2.extras import Json, execute_values
except ImportError:
    print("ERROR: psycopg2-binary is required. Install with: pip install psycopg2-binary")
    sys.exit(1)

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("ERROR: sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)

# ---- Configuration ----
EMBEDDING_MODEL = "all-MiniLM-L6-v2"   # 384-dimensional embeddings (change schema vector(384) if used)
CHUNK_SIZE = 500                       # characters per chunk
CHUNK_OVERLAP = 50

model = SentenceTransformer(EMBEDDING_MODEL)


def chunk_text(text, size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """Split text into overlapping chunks for embedding."""
    if not text:
        return []
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        chunks.append(text[start:end])
        if end >= len(text):
            break
        start = end - overlap
    return chunks


def load_content(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def ingest(conn, items):
    cur = conn.cursor()
    for item in items:
        # 1. Insert content item
        cur.execute(
            """
            INSERT INTO content_items (id, title, body_text, category, status)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
            """,
            (
                str(uuid.uuid4()),
                item.get("title", "Untitled"),
                item.get("body_text", ""),
                item.get("category", "general"),
                item.get("status", "published"),
            ),
        )
        content_id = cur.fetchone()[0]

        # 2. Insert images
        for idx, img in enumerate(item.get("images", [])):
            cur.execute(
                """
                INSERT INTO content_images (id, content_id, image_url, thumbnail_url, alt_text, position)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    str(uuid.uuid4()),
                    content_id,
                    img.get("url"),
                    img.get("thumbnail_url"),
                    img.get("alt_text", ""),
                    idx,
                ),
            )

        # 3. Chunk + embed body text for RAG
        body = item.get("body_text", "")
        for chunk in chunk_text(body):
            embedding = model.encode(chunk).tolist()
            cur.execute(
                """
                INSERT INTO knowledge_chunks (id, content_id, chunk_text, embedding, source_type)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (str(uuid.uuid4()), content_id, chunk, embedding, "content"),
            )

        # 4. Also create an FAQ entry if question/answer provided
        if item.get("question") and item.get("answer"):
            cur.execute(
                """
                INSERT INTO faqs (id, question, answer, related_content_ids, image_urls)
                VALUES (%s, %s, %s, (%s)::uuid[], %s)
                """,
                (
                    str(uuid.uuid4()),
                    item["question"],
                    item["answer"],
                    [content_id],
                    [img["url"] for img in item.get("images", [])],
                ),
            )

    conn.commit()
    cur.close()
    print(f"Ingested {len(items)} content items successfully.")


def main():
    parser = argparse.ArgumentParser(description="Ingest content into the customer KB")
    parser.add_argument("--file", required=True, help="Path to JSON content file")
    parser.add_argument("--db", required=True, help="PostgreSQL connection string")
    args = parser.parse_args()

    items = load_content(args.file)
    conn = psycopg2.connect(args.db)
    try:
        ingest(conn, items)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
