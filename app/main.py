from fastapi import FastAPI
from app.api import v1_router

def create_app() -> FastAPI:
    application = FastAPI(title="TeamIT API", version="1.0.0")
    application.include_router(v1_router.router, prefix="/api/v1")
    return application

app = create_app()
