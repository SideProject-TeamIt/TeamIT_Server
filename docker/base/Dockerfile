FROM python:3.12-slim as builder

WORKDIR /build

FROM python:3.12-slim

WORKDIR /app

RUN adduser --disabled-password --gecos "" appuser

RUN apt-get update && apt-get install -y curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PYTHONPATH="${PYTHONPATH}:/shared"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

USER appuser

CMD ["echo", "Base image - override this command"]