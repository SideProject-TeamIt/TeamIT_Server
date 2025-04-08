from fastapi import FastAPI
from app.router.team_router import router as team_router

from shared.config.base_config import BaseConfig
from shared.database.mongo import get_mongo_client

app = FastAPI()
app.include_router(team_router)

mongo_uri = BaseConfig.get_mongo_uri()
client = get_mongo_client(mongo_uri)
db = client[BaseConfig.MONGO_DB]
