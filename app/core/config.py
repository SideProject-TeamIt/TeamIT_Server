from pydantic_settings import BaseSettings
from functools import lru_cache
import os

class BaseConfig(BaseSettings):
    # 개발, 운영 관리
    ENV: str = "development"

    # 개발 url
    FRONTEND_URL: str
    BACKEND_URL: str
    BACKEND_VERSION: str

    # 데이터 베이스
    DATABASE_URL: str

    # JWT
    JWT_SECRET_KEY: str
    ALGORITHM: str = "HS256"

    # GOOGLE
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str

    # KAKAO
    KAKAO_CLIENT_ID: str
    KAKAO_CLIENT_SECRET: str

    # GITHUB
    GITHUB_CLIENT_ID: str
    GITHUB_CLIENT_SECRET: str

    class Config:
        env_file = ".env"

class DevConfig(BaseConfig):
    class Config:
        env_file = ".env.dev"

class ProdConfig(BaseConfig):
    class Config:
        env_file = ".env.prod"

@lru_cache()
def get_settings():
    env = os.getenv("ENV", "development")
    if env == "production":
        return ProdConfig()
    return DevConfig()

settings = get_settings()
