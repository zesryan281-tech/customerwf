# Multi-Channel Bot Setup Guide

Covers Telegram, WeChat Official Account, and Facebook Messenger.
All channels connect to the same backend: PostgreSQL/pgvector KB + RAG agent.

---

## 1. Telegram Bot

### Prerequisites
- Telegram account
- Bot token from @BotFather
- Public HTTPS webhook URL

### Setup Steps

1. **Create the bot**
   - Message [@BotFather](https://t.me/botfather) on Telegram
   - Send `/newbot`, follow prompts to choose name and username
   - Save the **Bot Token** (e.g. `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`)

2. **Set the webhook**
   ```
   POST https://api.telegram.org/bot<TOKEN>/setWebhook
   Body: { "url": "https://your-server.com/webhook/telegram" }
   ```
   - Telegram will POST JSON updates to your webhook on new messages
   - Verify: `GET https://api.telegram.org/bot<TOKEN>/getWebhookInfo`

3. **Receive messages**
   - Webhook receives `Update` objects containing `message`, `edited_message`, `callback_query`, etc.
   - Key fields: `update.message.chat.id`, `update.message.from.id`, `update.message.text`, `update.message.photo`

4. **Send replies**
   - Text: `POST https://api.telegram.org/bot<TOKEN>/sendMessage`
     ```json
     { "chat_id": 123456789, "text": "Hello!", "parse_mode": "Markdown" }
     ```
   - Photo: `POST https://api.telegram.org/bot<TOKEN>/sendPhoto`
     ```json
     { "chat_id": 123456789, "photo": "https://cdn.example.com/image.jpg", "caption": "..." }
     ```
   - Images can be sent as public URL or uploaded via `multipart/form-data`

5. **Images**
   - Store images in object storage (S3/MinIO/CDN)
   - Save URLs in `content_images` table
   - Send via `sendPhoto` with the public URL

### Pros
- Fast setup, no approval needed for basic bots
- Rich media (photos, documents, buttons)
- Global reach

### Cons
- Requires public HTTPS webhook
- Bot cannot initiate conversation (user must message first)

---

## 2. WeChat Official Account (Customer Service)

### Prerequisites
- WeChat Official Account (Service Account recommended for customer service)
- WeChat verification (¥300/year for service accounts)
- Public server to receive XML webhook callbacks

### Setup Steps

1. **Register account**
   - Go to [WeChat Official Account Platform](https://mp.weixin.qq.com/)
   - Register as Service Account (订阅号 = subscription, 服务号 = service)
   - Complete verification (business license required for service account)

2. **Configure server**
   - In WeChat MP platform: Basic Config → Set server URL, Token, EncodingAESKey
   - WeChat sends a GET request for validation (echo back `echostr`)
   - After validation, WeChat POSTs XML event callbacks to your URL

3. **Receive messages**
   - WeChat sends XML payloads for `message`, `subscribe`, `click`, etc.
   - Parse XML to extract: `FromUserName`, `ToUserName`, `MsgType`, `Content`, `PicUrl`, `MediaId`

4. **Send replies**
   - Customer Service API: `POST https://api.weixin.qq.com/cgi-bin/message/custom/send`
   - Requires `access_token` (from `GET https://api.weixin.qq.com/cgi-bin/token`)
   - Text message XML/JSON:
     ```json
     {
       "touser": "OPENID",
       "msgtype": "text",
       "text": { "content": "Hello!" }
     }
     ```
   - Image: upload media first (`media/upload`), then send with `media_id`

5. **Images**
   - Upload image to WeChat media server → get `media_id`
   - Send image message with `media_id`
   - `media_id` expires after 3 days; re-upload as needed

### Pros
- Huge reach in China
- Native WeChat experience
- Supports text, image, voice, video, mini-program cards

### Cons
- Requires Chinese business verification
- Webhook uses XML (not JSON)
- Customer service messages only within 48 hours of user's last message
- App review required for some features

---

## 3. Facebook Messenger

### Prerequisites
- Facebook Page
- Meta for Developers app with Messenger product
- Page Access Token
- Public HTTPS webhook URL

### Setup Steps

1. **Create app and page**
   - Create Facebook Page (if not exists)
   - Go to [Meta for Developers](https://developers.facebook.com/) → Create App
   - Add "Messenger" product to your app

2. **Configure webhook**
   - In app dashboard: Messenger → Settings → Webhooks → "Click to Subscribe"
   - Callback URL: `https://your-server.com/webhook/facebook`
   - Verify token: choose any string (e.g. `my_verify_token`)
   - Facebook sends GET `hub.challenge` — echo it back to verify
   - Subscribe to fields: `messages`, `messaging_postbacks`, `messaging_optins`, `messaging_referrals`

3. **Generate Page Access Token**
   - In app dashboard: Messenger → Settings → Token Generation
   - Select your Facebook Page
   - Copy the **Page Access Token** (starts with `EAAB...`)

4. **Receive messages**
   - Facebook POSTs JSON webhook events to your URL
   - Extract: `sender.id`, `recipient.id`, `message.text`, `message.attachments`
   - Acknowledge with HTTP 200

5. **Send replies**
   - Send API: `POST https://graph.facebook.com/v18.0/me/messages`
   ```json
   {
     "recipient": { "id": "PSID-123456789" },
     "message": { "text": "Hello!" }
   }
   ```
   - Query param: `?access_token=<PAGE_ACCESS_TOKEN>`
   - Image: `message.attachment = { type: "image", payload: { url: "https://..." } }` or `attachment_id` from upload

6. **Images**
   - Upload image: `POST https://graph.facebook.com/v18.0/me/message_attachments`
   - Get `attachment_id`, reuse for sending
   - Or send with public URL directly

### Pros
- Large user base, especially outside China
- Rich media support
- No verification needed for basic page bot

### Cons
- Requires App Review for `pages_messaging` and other permissions (production)
- Page-scoped user IDs (PSID) — users are page-specific
- Webhook must respond quickly (Facebook retries on timeout)

---

## 4. Unified Backend Architecture

```
┌─────────┐  webhook  ┌──────────────┐  normalized  ┌─────────────┐
│ Telegram│───────────▶│ Channel      │─────────────▶│ RAG Agent   │
│         │           │ Adapter      │              │ (KB Search) │
│ WeChat  │───────────▶│ (per channel)│              │             │
│         │           │              │              │ PostgreSQL  │
│ Facebook│───────────▶│              │              │ + pgvector  │
└─────────┘           └──────────────┘              └─────────────┘
```

Each channel adapter:
1. Receives platform-specific webhook
2. Normalizes to internal format: `{ channel, user_id, text, image_urls, ... }`
3. Calls RAG agent: search KB (SQL exact + vector semantic), generate answer
4. Sends reply via platform-specific send API

### Shared database tables used
- `customers` — map `channel + channel_user_id` to internal customer id
- `content_items` — articles, policies, product info
- `content_images` — image URLs + thumbnails
- `faqs` — exact Q&A pairs
- `knowledge_chunks` — vector embeddings for semantic search

---

## 5. Recommended Implementation Order

| Phase | Task | Channel |
|-------|------|---------|
| 1 | Provision PostgreSQL + pgvector; run `schema.sql` | All |
| 2 | Ingest content with `ingest.py` + `content.json` | All |
| 3 | Build Telegram bot + webhook adapter | Telegram |
| 4 | Build WeChat adapter (XML webhook + Customer Service API) | WeChat |
| 5 | Build Facebook adapter (webhook + Send API) | Facebook |
| 6 | Build unified RAG agent (SQL + vector search + LLM) | All |
| 7 | Deploy + test all three channels | All |

---

## 6. Files in This Workspace

| File | Purpose |
|------|---------|
| `schema.sql` | PostgreSQL + pgvector schema (content, images, FAQs, products, customers, RAG chunks) |
| `ingest.py` | Python ingestion script (JSON → DB, text chunking, embeddings) |
| `content.json` | Example content (shipping, password reset, return policy with image) |
| `channel-research.md` | This file — Telegram, WeChat, Facebook setup guides |
