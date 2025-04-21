import os
import sys

from fastapi import FastAPI
from app.router.auth_router import router as auth_router

from shared.config.settings import get_settings
from shared.config.base_config import BaseConfig
from shared.database.postgres import get_postgres_engine, get_postgres_session
from shared.utils.env_validator import validate_required_env_vars, get_postgres_required_vars

app = FastAPI()
app.include_router(auth_router)

# 환경 변수 검증
validate_required_env_vars(get_postgres_required_vars(), "auth-service")

# 환경변수 기반 URL
DATABASE_URL = BaseConfig.get_postgres_url()

engine = get_postgres_engine(DATABASE_URL)
SessionLocal = get_postgres_session(engine)