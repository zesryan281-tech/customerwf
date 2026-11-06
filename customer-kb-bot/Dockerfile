FROM python:3.11-slim

# The Flask support engine: RAG reply engine + Kestra-facing engine API.
# Runs on the same Docker network as Kestra so flows can call
# http://support-engine:5000/engine/* directly.

WORKDIR /app

RUN pip install --no-cache-dir \
      "flask>=3.0,<4" \
      "psycopg2-binary>=2.9" \
      "requests>=2.31"

COPY scripts/ /app/scripts/

ENV PORT=5000
EXPOSE 5000

# No shell, no build tools needed at runtime.
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:5000/health',timeout=4).status==200 else 1)"

CMD ["python", "scripts/webhook_server.py"]
