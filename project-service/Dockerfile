FROM python:3.11-slim

WORKDIR /app

# shared 모듈 복사 및 설치
COPY shared ./shared
RUN pip install --upgrade pip && pip install -e ./shared

# 서비스 의존성
COPY project-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 서비스 코드 복사
COPY project-service/app ./app
COPY project-service/tests ./tests

ENV PYTHONPATH="${PYTHONPATH}:/app"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
