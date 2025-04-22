from pydantic import BaseSettings
from functools import lru_cache
import os

class BaseConfig(BaseSettings):
    ENV: str = "development"
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    ALGORITHM: str = "HS256"

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
