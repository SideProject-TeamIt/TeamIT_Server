import os
import sys

from fastapi import FastAPI
from app.router.project_router import router as project_router

from shared.config.settings import get_settings
from shared.config.base_config import BaseConfig
from shared.database.mongo import get_mongo_client

app = FastAPI()
app.include_router(project_router)

mongo_uri = BaseConfig.get_mongo_uri()
client = get_mongo_client(mongo_uri)
db = client[BaseConfig.MONGO_DB]

# 환경 변수 검증
required_vars = ["MONGO_URI", "MONGO_DB"]
missing_vars = [var for var in required_vars if not os.getenv(var)]
if missing_vars:
    print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
    sys.exit(1)
