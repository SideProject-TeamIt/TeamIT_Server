FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 앱 모듈 복사
COPY app ./app
COPY tests ./tests
# 환경변수 (필요 시)
ENV PYTHONPATH="${PYTHONPATH}:/shared"

# FastAPI 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
