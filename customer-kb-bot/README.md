# Customer KB Bot — Multi-Channel Customer Answering Bot

## Overview

A multi-channel customer-answering bot backed by a PostgreSQL/pgvector knowledge base with RAG (Retrieval-Augmented Search). Built as an Agent Teams project with three members: researcher, engineer, and reviewer.

## Project Structure

```
customer-kb-bot/
├── README.md                 # This file — project overview and setup guide
├── db/
│   └── schema.sql            # PostgreSQL + pgvector schema (6 tables)
├── scripts/
│   └── ingest.py             # Python ingestion script (JSON → DB + embeddings)
├── content/
│   └── content.json          # Example content (FAQs, policies, products + images)
├── research/
│   └── channel-research.md   # Multi-channel setup guide (Telegram, WeChat, Facebook)
└── team-state/               # Agent Teams team state (for reference)
```

## Database Schema (`db/schema.sql`)

Six tables in PostgreSQL with pgvector:

| Table | Purpose |
|-------|---------|
| `content_items` | Articles, FAQs, policies, product descriptions |
| `content_images` | Image URLs + thumbnails (files stored in object storage) |
| `faqs` | Structured Q&A for exact-match SQL lookups |
| `products` | Product catalog with price, category, image |
| `customers` | Multi-channel customer mapping (channel + channel_user_id) |
| `knowledge_chunks` | RAG chunks with `vector(384)` embeddings + ivfflat index |

**Embedding model:** `all-MiniLM-L6-v2` (384 dimensions) — matches `ingest.py`

**Prerequisites:** PostgreSQL + pgvector extension + pgcrypto extension

## Ingestion Script (`scripts/ingest.py`)

Reads a JSON content file and inserts into PostgreSQL:
1. Inserts content items into `content_items`
2. Inserts images into `content_images`
3. Chunks body text, generates embeddings, inserts into `knowledge_chunks`
4. Creates FAQ entries if question/answer provided

**Usage:**
```bash
pip install psycopg2-binary sentence-transformers
python scripts/ingest.py --file content/content.json \
  --db "postgresql://user:pass@localhost:5433/kb"
```

## Content Example (`content/content.json`)

Three content items:
1. **Shipping Policy** — with image URL (shipping map)
2. **How to Reset Your Password** — FAQ-style with question/answer
3. **Return Policy** — 30-day return policy

## Channel Research (`research/channel-research.md`)

Step-by-step setup for three channels:

- **Telegram Bot:** @BotFather → bot token → webhook → sendMessage/sendPhoto
- **WeChat Official Account:** Service account + verification → XML webhook → Customer Service API
- **Facebook Messenger:** Meta app + Page → webhook → Send API

All channels connect to the same backend: channel adapter → normalized message → RAG agent → reply via platform API.

## Agent Teams Status

Team ID: `customer-kb-bot` | Web GUI: http://127.0.0.1:3080

| Task | Subject | Member | Status |
|------|---------|--------|--------|
| t1 | Telegram Bot API research | researcher | ✅ Completed |
| t2 | Database schema design | engineer | ✅ Completed (validated on PG 18) |
| t3 | Build ingestion script | engineer | 🔄 In progress (validating ingest.py end-to-end) |
| t4 | Review all deliverables | reviewer | ⏳ Pending (waits on t3 + t1) |

## Telegram Bot Token

**Token:** `8790668279:AAEVKmp-87yWTCGtWr2C-L3K2fxxUiw03ig`

**To set webhook:**
```bash
curl -X POST "https://api.telegram.org/bot8790668279:AAEVKmp-87yWTCGtWr2C-L3K2fxxUiw03ig/setWebhook" \
  -d "url=https://your-server.com/webhook/telegram"
```

## PostgreSQL Setup (Running)

PostgreSQL 18 is running on port 5433:
- Data directory: `/home/cndosks/.dsh/im/pgdata/`
- Socket directory: `/home/cndosks/.dsh/im/pg_socket/`
- Database: `kb`
- Schema already loaded: all 6 tables created

**Connect:**
```bash
psql -h /home/cndosks/.dsh/im/pg_socket -p 5433 -U cndosks -d kb
```

## Next Steps

1. Install Python deps: `pip install psycopg2-binary sentence-transformers`
2. Run ingestion: `python scripts/ingest.py --file content/content.json --db "postgresql://cndosks@localhost:5433/kb"`
3. Set Telegram webhook with your bot token
4. Wait for team t3/t4 to complete (reviewer will validate all deliverables)
5. Add WeChat and Facebook adapters using `research/channel-research.md`
