from motor.motor_asyncio import AsyncIOMotorClient
from shared.config.settings import settings

client = AsyncIOMotorClient(settings.mongo_uri)
mongo_db = client[settings.MONGO_DB]
