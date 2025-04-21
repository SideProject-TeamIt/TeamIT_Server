from fastapi import FastAPI
from .routers import gateway_router
import logging

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

app = FastAPI(title="TeamIT API Gateway")

@app.get("/")
def read_root():
    return {"message": "여기는 api-gateway 페이지입니다"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# 게이트웨이 라우터 등록
app.include_router(gateway_router.router)