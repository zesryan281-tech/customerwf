-- Customer Knowledge Base Schema
-- Supports text + image content, RAG vector search, and multi-channel customers.
-- Database: PostgreSQL with pgvector extension
--
-- Prerequisites (must be installed in the target PostgreSQL cluster):
--   - pgvector  (provides the `vector` type + ivfflat/HNSW indexes)
--   - pgcrypto  (provides gen_random_uuid(); ships with PostgreSQL)
-- Embedding model: all-MiniLM-L6-v2 -> 384-dimensional vectors (see ingest.py)
--
-- Scope: text content (content_items, faqs, products), image content
-- (content_images), RAG chunks with embeddings (knowledge_chunks), and
-- multi-channel customers (customers: telegram, wechat, facebook, extensible).

-- ---------------------------------------------------------------------------
-- Extensions
-- ---------------------------------------------------------------------------
-- pgcrypto is bundled with PostgreSQL. pgvector must be installed separately;
-- uncomment the vector line once the pgvector extension is available in the
-- target cluster (required before knowledge_chunks can be created).
CREATE EXTENSION IF NOT EXISTS pgcrypto;
-- CREATE EXTENSION IF NOT EXISTS vector;

-- ---------------------------------------------------------------------------
-- Top-level content items (FAQs, articles, policies, product descriptions)
-- ---------------------------------------------------------------------------
CREATE TABLE content_items (
    id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title          TEXT NOT NULL,
    body_text      TEXT,
    category       VARCHAR(100),
    status         VARCHAR(50) DEFAULT 'published', -- published, draft, archived
    search_tsv     TSVECTOR
                   GENERATED ALWAYS AS (
                       to_tsvector('english',
                           coalesce(title, '') || ' ' || coalesce(body_text, ''))
                   ) STORED,
    created_at     TIMESTAMPTZ DEFAULT now(),
    updated_at     TIMESTAMPTZ DEFAULT now()
);

-- ---------------------------------------------------------------------------
-- Images attached to content items (stored in object storage; only URLs kept)
-- ---------------------------------------------------------------------------
CREATE TABLE content_images (
    id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    content_id     UUID NOT NULL REFERENCES content_items(id) ON DELETE CASCADE,
    image_url      TEXT NOT NULL,
    thumbnail_url  TEXT,
    alt_text       TEXT,
    position       INTEGER DEFAULT 0,
    created_at     TIMESTAMPTZ DEFAULT now()
);

-- ---------------------------------------------------------------------------
-- Structured FAQs (exact-match SQL lookups)
-- ---------------------------------------------------------------------------
CREATE TABLE faqs (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    question          TEXT NOT NULL,
    answer            TEXT NOT NULL,
    related_content_ids UUID[],
    image_urls        TEXT[],
    created_at        TIMESTAMPTZ DEFAULT now()
);

-- ---------------------------------------------------------------------------
-- Product catalog
-- ---------------------------------------------------------------------------
CREATE TABLE products (
    id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name           TEXT NOT NULL,
    description    TEXT,
    price          NUMERIC(12, 2),
    image_url      TEXT,
    category_id    UUID, -- loose reference; no dedicated categories table yet
    created_at     TIMESTAMPTZ DEFAULT now()
);

-- ---------------------------------------------------------------------------
-- Customers (personalization across channels: telegram, wechat, facebook)
-- ---------------------------------------------------------------------------
CREATE TABLE customers (
    id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name           TEXT,
    channel        VARCHAR(50) NOT NULL, -- telegram, wechat, facebook, ...
    channel_user_id TEXT NOT NULL,        -- platform-specific user id
    preferences    JSONB DEFAULT '{}',
    last_seen      TIMESTAMPTZ DEFAULT now(),
    UNIQUE (channel, channel_user_id)
);

-- ---------------------------------------------------------------------------
-- RAG chunks with embeddings for semantic search
-- ---------------------------------------------------------------------------
CREATE TABLE knowledge_chunks (
    id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    content_id     UUID NOT NULL REFERENCES content_items(id) ON DELETE CASCADE,
    chunk_text     TEXT NOT NULL,
    embedding      vector(384), -- matches all-MiniLM-L6-v2 used by ingest.py
    source_type    VARCHAR(50) DEFAULT 'content', -- content, faq, product
    created_at     TIMESTAMPTZ DEFAULT now()
);

-- ---------------------------------------------------------------------------
-- Indexes for common query patterns
-- ---------------------------------------------------------------------------
-- Semantic (cosine) search over embeddings. Requires pgvector.
CREATE INDEX idx_knowledge_chunks_embedding
    ON knowledge_chunks USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
-- Hybrid keyword search over title + body_text.
CREATE INDEX idx_content_items_search_tsv ON content_items USING gin (search_tsv);
-- FK / lookup indexes.
CREATE INDEX idx_content_images_content ON content_images(content_id);
CREATE INDEX idx_faqs_related_content ON faqs USING gin (related_content_ids);
CREATE INDEX idx_knowledge_chunks_content ON knowledge_chunks(content_id);
CREATE INDEX idx_customers_channel_user ON customers(channel, channel_user_id);

-- ---------------------------------------------------------------------------
-- Updated-at trigger for content_items
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_content_items_updated_at
BEFORE UPDATE ON content_items
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

-- ---------------------------------------------------------------------------
-- support_events — inbound questions, answers, and escalation state.
-- Written by the Flask engine (webhook + /engine/rag with record=true) and read
-- by the Kestra escalation flow (/engine/escalations).
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS support_events (
    id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id      UUID REFERENCES customers(id) ON DELETE SET NULL,
    channel          VARCHAR(50) NOT NULL DEFAULT 'telegram',
    channel_user_id  TEXT NOT NULL,
    question         TEXT NOT NULL,
    answer           TEXT,
    source           VARCHAR(30), -- faq | content | semantic | fallback | error
    answered         BOOLEAN NOT NULL DEFAULT FALSE,
    escalated_at     TIMESTAMPTZ,
    resolved_at      TIMESTAMPTZ,
    created_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Open escalations are looked up by age; partial index keeps it cheap.
CREATE INDEX IF NOT EXISTS support_events_open_idx
    ON support_events (created_at) WHERE resolved_at IS NULL;
CREATE INDEX IF NOT EXISTS support_events_customer_idx
    ON support_events (channel, channel_user_id, created_at DESC);

-- ---------------------------------------------------------------------------
-- Example data (mirrors content.json)
-- ---------------------------------------------------------------------------
INSERT INTO faqs (question, answer) VALUES
('How do I reset my password?', 'You can reset your password on the login page by clicking "Forgot password" and following the email instructions.');

INSERT INTO content_items (title, body_text, category) VALUES
('Shipping Policy', 'We ship worldwide. Standard delivery takes 5-7 business days. Express delivery takes 2-3 business days. Free shipping on orders over $50.', 'policy');
