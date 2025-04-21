# 빌드 스테이지
FROM python:3.12-slim as builder

WORKDIR /build

# 의존성 파일 복사 및 wheel 생성
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /build/wheels -r requirements.txt

# 실행 스테이지
FROM python:3.12-slim

WORKDIR /app

# 보안을 위한 비특권 사용자 생성
RUN adduser --disabled-password --gecos "" appuser

# curl 설치 (healthcheck 용)
RUN apt-get update && apt-get install -y curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 빌드 스테이지에서 생성된 wheel 파일 복사 및 설치
COPY --from=builder /build/wheels /wheels
RUN pip install --no-cache /wheels/*

# 앱 코드 복사
COPY app ./app
COPY tests ./tests

# 환경변수 설정
ENV PYTHONPATH="${PYTHONPATH}:/shared"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 헬스체크 엔드포인트 추가
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# 사용자 전환
USER appuser

# FastAPI 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]