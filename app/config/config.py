import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost:5432/mydatabase")

    class Config:
        env_file = ".env"  # 환경 변수 파일 로드 (선택 사항)

settings = Settings()
