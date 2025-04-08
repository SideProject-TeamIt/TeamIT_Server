from fastapi import FastAPI
from app.router.auth_router import router as auth_router

from shared.config.base_config import BaseConfig
from shared.database.postgres import get_postgres_engine, get_postgres_session

app = FastAPI()
app.include_router(auth_router)

# 환경변수 기반 URL
DATABASE_URL = BaseConfig.get_postgres_url()

engine = get_postgres_engine(DATABASE_URL)
SessionLocal = get_postgres_session(engine)
