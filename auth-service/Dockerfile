# 1. 공식 Python 이미지 사용 (slim으로 경량화)
FROM python:3.12-slim

# 2. 환경 변수 설정 (버퍼링 비활성화, UTF-8 보장)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

# 3. 작업 디렉토리 생성 및 이동
WORKDIR /app

# 4. 시스템 패키지 최소 설치 (보안 및 빌드 성능 개선)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential gcc netcat && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 5. requirements 미리 복사해 캐시 활용
COPY requirements.txt .

# 6. 의존성 설치 (캐시 최적화 + 보안)
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 7. 실제 애플리케이션 코드 복사
COPY app ./app

# 8. Uvicorn 서버 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
