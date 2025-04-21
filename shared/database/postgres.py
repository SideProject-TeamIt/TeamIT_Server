from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta
from fastapi import Depends
from typing import Generator
import logging

Base: DeclarativeMeta = declarative_base()
logger = logging.getLogger(__name__)

class PostgresClient:
    def __init__(self, database_url: str, pool_size: int = 5, max_overflow: int = 10):
        self.engine = create_engine(
            database_url,
            pool_pre_ping=True,
            pool_size=pool_size,
            max_overflow=max_overflow
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        logger.info(f"PostgreSQL connection initialized to {database_url.split('@')[-1]}")

    def create_tables(self):
        """테이블 생성"""
        Base.metadata.create_all(bind=self.engine)
        logger.info("PostgreSQL tables created")

    def get_db(self) -> Generator:
        """데이터베이스 세션 의존성"""
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def check_connection(self) -> bool:
        """데이터베이스 연결 확인 (헬스체크용)"""
        try:
            with self.engine.connect() as conn:
                conn.execute("SELECT 1")
            return True
        except Exception as e:
            logger.error(f"Database connection check failed: {e}")
            return False