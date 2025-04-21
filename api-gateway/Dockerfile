# 빌드 스테이지
FROM python:3.12-slim as builder

WORKDIR /build

# 의존성 파일 복사 및 wheel 생성
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /build/wheels -r requirements.txt

# 베이스 이미지 사용
FROM teamit/base:latest

# 빌드 스테이지에서 생성된 wheel 파일 복사 및 설치
COPY --from=builder /build/wheels /wheels
RUN pip install --no-cache /wheels/*

# 앱 코드 복사
COPY app ./app

# FastAPI 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]