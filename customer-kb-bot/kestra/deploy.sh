#!/usr/bin/env bash
# Deploy Kestra flows from ./flows to a running Kestra instance.
#
#   ./deploy.sh                     # deploy every flows/*.yaml
#   ./deploy.sh flows/foo.yaml ...  # deploy specific files
#
# Kestra's write API is tenant-scoped and YAML-only, which is easy to miss:
#   POST   /api/v1/main/flows                Content-Type: application/x-yaml
#   PUT    /api/v1/main/flows/{ns}/{id}      Content-Type: application/x-yaml
#   POST   /api/v1/main/namespaces           Content-Type: application/x-yaml
#   GET    /api/v1/main/flows/{ns}/{id}      (read)
# The un-prefixed /api/v1/flows is the read-only surface.
#
# Env: KESTRA_URL  (default http://127.0.0.1:8080)
#      KESTRA_USER / KESTRA_PASS
set -euo pipefail

KESTRA_URL="${KESTRA_URL:-http://127.0.0.1:8080}"
KESTRA_USER="${KESTRA_USER:-aiizxcvbnm9911@gmail.com}"
KESTRA_PASS="${KESTRA_PASS:-Zxcvbnm123@}"
API="${KESTRA_URL}/api/v1/main"
AUTH=(-u "${KESTRA_USER}:${KESTRA_PASS}")
YAML=(-H 'Content-Type: application/x-yaml')

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

ensure_namespace() {
  local ns="$1" code
  code="$(curl -s "${AUTH[@]}" -o /dev/null -w '%{http_code}' -X POST "${API}/namespaces" \
    "${YAML[@]}" --data-binary "id: ${ns}")"
  case "$code" in
    200|201|409) return 0 ;;
    *) echo "  warn namespace ${ns}: HTTP ${code}" ;;
  esac
}

deploy_one() {
  local file="$1" ns id code
  ns="$(grep -E '^namespace:' "$file" | head -1 | sed 's/^namespace:[[:space:]]*//')"
  id="$(grep -E '^id:' "$file" | head -1 | sed 's/^id:[[:space:]]*//')"
  ensure_namespace "$ns"

  # PUT updates an existing flow; fall back to POST for a first deployment.
  code="$(curl -s "${AUTH[@]}" -o /tmp/.kestra_deploy_err -w '%{http_code}' -X PUT \
    "${API}/flows/${ns}/${id}" "${YAML[@]}" --data-binary "@${file}")"
  if [[ "$code" != "200" && "$code" != "201" ]]; then
    code="$(curl -s "${AUTH[@]}" -o /tmp/.kestra_deploy_err -w '%{http_code}' -X POST \
      "${API}/flows" "${YAML[@]}" --data-binary "@${file}")"
  fi

  if [[ "$code" == "200" || "$code" == "201" ]]; then
    echo "  ok   ${ns}/${id}  (${file##*/})"
  else
    echo "  FAIL ${ns}/${id}  (${file##*/}) -> HTTP ${code}"
    head -c 600 /tmp/.kestra_deploy_err 2>/dev/null || true
    echo
    return 1
  fi
}

if [[ $# -gt 0 ]]; then files=("$@"); else files=("${here}"/flows/*.yaml); fi

echo "Deploying to ${KESTRA_URL}"
for f in "${files[@]}"; do deploy_one "$f"; done
