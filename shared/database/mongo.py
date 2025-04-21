from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

class MongoClient:
    def __init__(self, mongo_uri: str, db_name: str):
        self.client = AsyncIOMotorClient(mongo_uri)
        self.db = self.client[db_name]
        logger.info(f"MongoDB connection initialized to {mongo_uri.split('//')[-1]}/{db_name}")

    def get_collection(self, collection_name: str):
        """컬렉션 가져오기"""
        return self.db[collection_name]

    async def check_connection(self) -> bool:
        """데이터베이스 연결 확인 (헬스체크용)"""
        try:
            await self.db.command("ping")
            return True
        except Exception as e:
            logger.error(f"MongoDB connection check failed: {e}")
            return False