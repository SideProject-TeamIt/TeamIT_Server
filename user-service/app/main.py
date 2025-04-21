import os
import sys

from fastapi import FastAPI
from app.router.user_router import router as user_router

from shared.config.settings import get_settings
from shared.config.base_config import BaseConfig
from shared.database.postgres import get_postgres_engine, get_postgres_session

app = FastAPI()
app.include_router(user_router)

# 환경변수 기반 URL
DATABASE_URL = BaseConfig.get_postgres_url()

engine = get_postgres_engine(DATABASE_URL)
SessionLocal = get_postgres_session(engine)


# 환경 변수 검증
required_vars = ["POSTGRES_USER", "POSTGRES_PASSWORD", "POSTGRES_DB"]
missing_vars = [var for var in required_vars if not os.getenv(var)]
if missing_vars:
    print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
    sys.exit(1)