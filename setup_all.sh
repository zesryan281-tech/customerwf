#!/bin/bash
#
# setup_all.sh — ONE-COMMAND startup for the @spdhdod_bot hybrid support stack.
#
# After ANY laptop restart (or whenever the bot seems dead), the ONLY command:
#
#     cd /home/cndosks/.dsh/im && ./setup_all.sh
#
# Everything long-running now lives in Docker with restart=unless-stopped, so
# all containers auto-start on boot and this script spawns NO background
# processes of its own — safe to run from any terminal, twice, anytime.
#
#   kb-postgres     KB database (PostgreSQL 18, port 5433 + socket)  auto-starts
#   kestra-postgres Kestra metadata DB                               auto-starts
#   kestra          Orchestrator + UI on http://127.0.0.1:8080       auto-starts
#   support-engine  Flask RAG engine on http://127.0.0.1:5000        auto-starts
#   kb-tunnel       Cloudflare tunnel → Kestra :8080                  auto-starts
#
# The script therefore only: starts stopped containers (creates missing ones),
# waits for health, re-deploys flows if missing, and re-registers the Telegram
# webhook — the one thing that can never auto-heal, because trycloudflare
# URLs change on every boot.
#
# Architecture: Telegram → tunnel → Kestra → HTTP → support-engine → Telegram
#
set -uo pipefail

WORKDIR="/home/cndosks/.dsh/im"
BOT_TOKEN="8790668279:AAEVKmp-87yWTCGtWr2C-L3K2fxxUiw03ig"
WEBHOOK_PATH="/api/v1/executions/webhook/customer-support/customer-auto-reply/telegram-reply"
PG_CTL="/usr/lib/postgresql/18/bin/pg_ctl"
PGDATA="$WORKDIR/pgdata"
PGSOCKET="$WORKDIR/pg_socket"
KESTRA_URL="http://127.0.0.1:8080"
KESTRA_USER="aiizxcvbnm9911@gmail.com"
KESTRA_PASS="Zxcvbnm123@"
ENGINE_URL="http://127.0.0.1:5000"

command -v psql >/dev/null 2>&1 || export PATH="$PATH:/usr/lib/postgresql/18/bin"
export PGHOST="$PGSOCKET" PGPORT=5433 PGDATABASE=kb PGUSER=cndosks

pg_up() { psql -tAc 'SELECT 1' >/dev/null 2>&1; }

wait_http() { # $1=url  $2=tries  $3=sleep-seconds
  local i; for ((i=0; i<$2; i++)); do
    curl -s -o /dev/null --max-time 3 "$1" && return 0
    sleep "$3"
  done
  return 1
}

echo "===================================================="
echo "  @spdhdod_bot — one-command startup (hybrid stack)"
echo "===================================================="

# ---------------------------------------------------------------------------
echo ""
echo "[1/6] Waiting for Docker daemon..."
DK=""
for i in $(seq 1 30); do docker info >/dev/null 2>&1 && { DK=1; break; }; sleep 1; done
[ -n "$DK" ] || { echo "  ERROR: Docker is not running. Start it once: sudo systemctl start docker"; exit 1; }
echo "      Docker is up."

# ---------------------------------------------------------------------------
echo ""
echo "[2/6] KB database (PostgreSQL 18, port 5433)..."
if pg_up; then
  echo "      KB database already answering."
else
  # Stale pid/socket files left by a dead instance (safe: PG just failed to answer)
  rm -f "$PGDATA/postmaster.pid" "$PGSOCKET"/.s.PGSQL.5433 "$PGSOCKET"/.s.PGSQL.5433.lock 2>/dev/null || true

  if docker inspect kb-postgres >/dev/null 2>&1; then
    echo "      kb-postgres: starting container..."
    docker start kb-postgres >/dev/null 2>&1 || true
  else
    echo "      kb-postgres: creating container..."
    docker run -d --name kb-postgres --restart unless-stopped --network host \
      --user 1000:1000 \
      -v "$PGDATA":/var/lib/postgresql/data \
      -v "$PGSOCKET":/var/run/postgresql \
      postgres:18 -p 5433 -c listen_addresses=localhost \
                  -c unix_socket_directories=/var/run/postgresql >/dev/null 2>&1 || true
  fi
  for i in $(seq 1 15); do pg_up && break; sleep 2; done

  if ! pg_up; then
    echo "      Container failed — falling back to host pg_ctl..."
    "$PG_CTL" -D "$PGDATA" -o "-p 5433 -c unix_socket_directories='$PGSOCKET'" \
      -l "$WORKDIR/pg.log" start -w 2>&1 || true
    for i in $(seq 1 15); do pg_up && break; sleep 2; done
  fi
fi
pg_up && echo "      KB database: UP ($(psql -tAc 'SELECT count(*) FROM content_items;' 2>/dev/null) content_items)" \
      || { echo "  ERROR: KB database did not start. Logs: docker logs kb-postgres / $WORKDIR/pg.log"; exit 1; }

# ---------------------------------------------------------------------------
echo ""
echo "[3/6] Containers: kestra-postgres, kestra, support-engine..."

start_or_create() { # $1=name ; remaining args = docker run spec when missing
  local name=$1; shift
  if docker inspect "$name" >/dev/null 2>&1; then
    if [ "$(docker inspect -f '{{.State.Running}}' "$name")" != "true" ]; then
      echo "      $name: starting..."
      docker start "$name" >/dev/null || { echo "  ERROR: could not start $name"; return 1; }
    else
      echo "      $name: already running"
    fi
  else
    echo "      $name: missing — recreating..."
    "$@" >/dev/null || { echo "  ERROR: could not create $name"; return 1; }
  fi
  return 0
}

docker update --restart unless-stopped support-engine >/dev/null 2>&1 || true

start_or_create kestra-postgres \
  docker run -d --name kestra-postgres --restart unless-stopped \
    -v kestra_pgdata:/var/lib/postgresql/data -e POSTGRES_PASSWORD=Zxcvbnm123@ \
    -e POSTGRES_DB=kestra postgres:17 \
  || exit 1

start_or_create kestra \
  docker run -d --name kestra --restart unless-stopped \
    --network kestra-facebook_kestra-network --network-alias kestra \
    -p 8080:8080 --link kestra-postgres:postgres \
    kestra/kestra:2.0.3 server local \
    --configuration /app/configuration.yml \
  || exit 1

start_or_create support-engine \
  docker run -d --name support-engine --restart unless-stopped \
    --network kestra-facebook_kestra-network -p 5000:5000 \
    -v "$PGSOCKET":/pg_socket \
    -e TELEGRAM_BOT_TOKEN="$BOT_TOKEN" \
    -e "DATABASE_URL=postgresql://cndosks@localhost:5433/kb?host=/pg_socket&port=5433" \
    -e SUPPORT_CHAT_ID=6009345177 \
    support-engine:local \
  || exit 1

# ---------------------------------------------------------------------------
echo ""
echo "[4/6] Waiting for Kestra and the RAG engine..."
wait_http "$KESTRA_URL" 90 2 || { echo "  ERROR: Kestra did not come up. Logs: docker logs kestra"; exit 1; }
echo "      Kestra is up."

FLOW_CODE=$(curl -s -u "$KESTRA_USER:$KESTRA_PASS" -o /dev/null -w '%{http_code}' \
  "$KESTRA_URL/api/v1/main/flows/customer-support/customer-auto-reply")
if [ "$FLOW_CODE" != "200" ]; then
  echo "      customer-auto-reply flow missing (HTTP $FLOW_CODE) — re-deploying all flows..."
  (cd "$WORKDIR/customer-kb-bot/kestra" && bash deploy.sh) || echo "      WARNING: flow deploy reported errors"
else
  echo "      Flows are deployed."
fi

ENGINE_OK=""
for i in $(seq 1 45); do
  curl -sf --max-time 5 "$ENGINE_URL/health" >/dev/null 2>&1 && { ENGINE_OK=1; break; }
  sleep 2
done
[ -n "$ENGINE_OK" ] && echo "      RAG engine: $(curl -s --max-time 5 "$ENGINE_URL/health")" \
  || { echo "  ERROR: RAG engine not healthy. Logs: docker logs support-engine"; exit 1; }

# ---------------------------------------------------------------------------
echo ""
echo "[5/6] Cloudflare tunnel → Kestra (8080)..."
get_url_from_docker() {
  docker logs --tail 300 kb-tunnel 2>&1 \
    | grep -o 'https://[a-zA-Z0-9.-]*\.trycloudflare\.com' | tail -1
}

if docker inspect kb-tunnel >/dev/null 2>&1; then
  [ "$(docker inspect -f '{{.State.Running}}' kb-tunnel)" = "true" ] || docker start kb-tunnel >/dev/null
  TUNNEL=docker
else
  if docker run -d --name kb-tunnel --restart unless-stopped --network host \
      cloudflare/cloudflared:latest tunnel --url http://127.0.0.1:8080 >/dev/null 2>&1; then
    TUNNEL=docker
  else
    echo "      (image unavailable — using local cloudflared binary)"
    TUNNEL=binary
  fi
fi

CF_URL=""
if [ "$TUNNEL" = "docker" ]; then
  for i in $(seq 1 45); do CF_URL=$(get_url_from_docker); [ -n "$CF_URL" ] && break; sleep 1; done
else
  pkill -f cloudflared 2>/dev/null || true; sleep 1
  : > "$WORKDIR/cloudflared.log"
  nohup "$WORKDIR/cloudflared" tunnel --url http://127.0.0.1:8080 \
    > "$WORKDIR/cloudflared.log" 2>&1 &
  for i in $(seq 1 45); do
    CF_URL=$(grep -o 'https://[a-zA-Z0-9.-]*\.trycloudflare\.com' "$WORKDIR/cloudflared.log" 2>/dev/null | head -1)
    [ -n "$CF_URL" ] && break; sleep 1
  done
fi
[ -n "$CF_URL" ] || { echo "  ERROR: no tunnel URL found. Logs: docker logs kb-tunnel"; exit 1; }
echo "      Tunnel URL: $CF_URL"

# Is that URL actually alive? (stale URL can linger in logs after a crash)
probe_tunnel() { # $1 = full webhook url
  [ "$(curl -s -o /dev/null -w '%{http_code}' --max-time 15 -X POST "$1" \
       -H 'Content-Type: application/json' -d '{}')" = "200" ]
}

WEBHOOK_URL="${CF_URL}${WEBHOOK_PATH}"
if ! probe_tunnel "$WEBHOOK_URL"; then
  echo "      Tunnel not answering yet — restarting it for a fresh URL..."
  if [ "$TUNNEL" = "docker" ]; then
    docker restart kb-tunnel >/dev/null
    OLD_URL="$CF_URL"
    for i in $(seq 1 45); do
      CF_URL=$(get_url_from_docker)
      { [ -n "$CF_URL" ] && [ "$CF_URL" != "$OLD_URL" ]; } && break
      sleep 1
    done
  else
    pkill -f cloudflared 2>/dev/null || true; sleep 1
    : > "$WORKDIR/cloudflared.log"
    nohup "$WORKDIR/cloudflared" tunnel --url http://127.0.0.1:8080 \
      > "$WORKDIR/cloudflared.log" 2>&1 &
    for i in $(seq 1 45); do
      CF_URL=$(grep -o 'https://[a-zA-Z0-9.-]*\.trycloudflare\.com' "$WORKDIR/cloudflared.log" 2>/dev/null | head -1)
      [ -n "$CF_URL" ] && break; sleep 1
    done
  fi
  [ -n "$CF_URL" ] || { echo "  ERROR: tunnel restart failed."; exit 1; }
  WEBHOOK_URL="${CF_URL}${WEBHOOK_PATH}"
  echo "      New tunnel URL: $CF_URL"
fi

# ---------------------------------------------------------------------------
echo ""
echo "[6/6] Telegram webhook..."
REGISTERED=$(curl -s --max-time 15 "https://api.telegram.org/bot${BOT_TOKEN}/getWebhookInfo" \
  | grep -o '"url":"[^"]*"' | head -1 | cut -d'"' -f4)
if [ "$REGISTERED" = "$WEBHOOK_URL" ]; then
  echo "      Webhook already points at the live tunnel — nothing to do."
else
  SET=$(curl -s --max-time 15 -X POST "https://api.telegram.org/bot${BOT_TOKEN}/setWebhook" \
    -H "Content-Type: application/json" -d "{\"url\":\"${WEBHOOK_URL}\"}")
  echo "      setWebhook: $SET"
fi

# Final verification with warm-up retries
SMOKE=""; SM_OK=""
for i in $(seq 1 5); do
  SMOKE=$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 -X POST "$WEBHOOK_URL" \
    -H 'Content-Type: application/json' -d '{}')
  [ "$SMOKE" = "200" ] && { SM_OK=1; break; }
  sleep 6
done
[ -n "$SM_OK" ] && echo "      Verified: public webhook answered HTTP 200." \
  || echo "      WARNING: smoke test got HTTP $SMOKE (tunnel cold). Re-run this script in ~1 min."

INFO=$(curl -s --max-time 15 "https://api.telegram.org/bot${BOT_TOKEN}/getWebhookInfo")
PENDING=$(echo "$INFO" | grep -o '"pending_update_count":[0-9]*' | head -1)

echo ""
echo "===================================================="
echo "  SETUP COMPLETE — @spdhdod_bot is live"
echo "===================================================="
echo "Webhook:    $WEBHOOK_URL"
echo "Kestra UI:  http://127.0.0.1:8080  (user $KESTRA_USER)"
echo "Engine:     $ENGINE_URL/health"
echo "Telegram:   webhook registered, $PENDING"
echo ""
echo "After your next reboot all containers start by themselves —"
echo "just run this script again to refresh the webhook:"
echo "    cd $WORKDIR && ./setup_all.sh"
