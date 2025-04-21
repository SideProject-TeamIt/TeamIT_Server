from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .router.gateway_router import router
import logging

app = FastAPI(title="TeamIT API Gateway")

# CORS 설정
app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "여기는 api-gateway 페이지입니다"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "api-gateway"}

# v1 API 라우터 등록
app.include_router(router, prefix="/v1")  # gateway_router.router에서 router로 변경