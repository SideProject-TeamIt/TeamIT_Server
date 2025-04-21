import os
import sys

from fastapi import FastAPI
from app.router.project_router import router

from shared.config.settings import get_settings
from shared.config.base_config import BaseConfig
from shared.database.mongo import get_mongo_client
from shared.utils.env_validator import validate_required_env_vars, get_postgres_required_vars

app = FastAPI()
app.include_router(router)

# MongoDB 연결 설정
mongo_uri = BaseConfig.get_mongo_uri()
client = get_mongo_client(mongo_uri)
db = client[BaseConfig.MONGO_DB]

# 환경 변수 검증
validate_required_env_vars(get_postgres_required_vars(), "project-service")