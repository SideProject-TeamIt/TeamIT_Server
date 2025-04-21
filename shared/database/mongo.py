from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

# 전역 클라이언트 인스턴스
_mongo_client = None
_mongo_db = None

def get_mongo_client(mongo_uri: str = None):
    """MongoDB 클라이언트 인스턴스 반환 (싱글톤 패턴)"""
    global _mongo_client
    if _mongo_client is None and mongo_uri is not None:
        _mongo_client = AsyncIOMotorClient(mongo_uri)
        logger.info(f"MongoDB connection initialized to {mongo_uri.split('//')[-1]}")
    return _mongo_client

def get_mongo_db(db_name: str = None):
    """MongoDB 데이터베이스 인스턴스 반환"""
    global _mongo_client, _mongo_db
    if _mongo_db is None and db_name is not None and _mongo_client is not None:
        _mongo_db = _mongo_client[db_name]
        logger.info(f"MongoDB database selected: {db_name}")
    return _mongo_db

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