from fastapi import FastAPI
from app.router.project_router import router as project_router

from shared.config.base_config import BaseConfig
from shared.database.mongo import get_mongo_client

app = FastAPI()
app.include_router(project_router)

mongo_uri = BaseConfig.get_mongo_uri()
client = get_mongo_client(mongo_uri)
db = client[BaseConfig.MONGO_DB]
