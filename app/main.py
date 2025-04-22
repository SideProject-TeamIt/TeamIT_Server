from fastapi import FastAPI
from app.api import v1_router

def create_app() -> FastAPI:
    app = FastAPI(title="TeamIT API", version="1.0.0")

    app.include_router(v1_router.router, prefix="/api/v1")

    return app

app = create_app()
