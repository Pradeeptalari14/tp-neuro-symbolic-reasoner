FROM python:3.11-slim-bookworm

WORKDIR /app

RUN useradd -r -u 1001 -g root appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chown -R appuser:root /app && chmod -R 755 /app

USER appuser

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD python -c "import sys; sys.exit(0)"

ENTRYPOINT ["python", "main.py"]
