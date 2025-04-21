from pydantic import BaseSettings, Field
from typing import Dict, Any, Optional
import os
from functools import lru_cache


class DatabaseSettings(BaseSettings):
    """데이터베이스 설정 기본 클래스"""
    pass


class PostgresSettings(DatabaseSettings):
    """PostgreSQL 설정"""
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432

    @property
    def postgres_uri(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


class MongoSettings(DatabaseSettings):
    """MongoDB 설정"""
    MONGO_DB: str = "admin"
    MONGO_HOST: str = "mongodb"
    MONGO_PORT: int = 27017

    @property
    def mongo_uri(self) -> str:
        return f"mongodb://{self.MONGO_HOST}:{self.MONGO_PORT}"


class JWTSettings(BaseSettings):
    """JWT 인증 설정"""
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 60


class ServiceSettings(BaseSettings):
    """서비스 URL 설정"""
    AUTH_SERVICE_URL: str = "http://auth-service:8000"
    USER_SERVICE_URL: str = "http://user-service:8000"
    TEAM_SERVICE_URL: str = "http://team-service:8000"
    PROJECT_SERVICE_URL: str = "http://project-service:8000"
    NOTIFICATION_SERVICE_URL: str = "http://notification-service:8000"


class BaseAppSettings(BaseSettings):
    """
    모든 서비스의 기본 설정 클래스
    """
    APP_NAME: str
    DEBUG: bool = Field(default=False)

    # 환경변수 파일 경로
    class Config:
        env_file = ".env"


@lru_cache()
def get_settings(service_name: str) -> Any:
    """
    서비스 이름에 따라 적절한 설정 클래스의 인스턴스를 반환합니다.
    캐싱을 통해 성능을 최적화합니다.
    """
    settings_map = {
        "auth": AuthServiceSettings,
        "user": UserServiceSettings,
        "team": TeamServiceSettings,
        "project": ProjectServiceSettings,
        "notification": NotificationServiceSettings,
        "api-gateway": APIGatewaySettings
    }

    if service_name not in settings_map:
        raise ValueError(f"Unknown service: {service_name}")

    return settings_map[service_name]()


# 서비스별 설정 클래스
class AuthServiceSettings(BaseAppSettings, PostgresSettings, JWTSettings):
    APP_NAME: str = "auth-service"


class UserServiceSettings(BaseAppSettings, PostgresSettings):
    APP_NAME: str = "user-service"


class TeamServiceSettings(BaseAppSettings, MongoSettings):
    APP_NAME: str = "team-service"


class ProjectServiceSettings(BaseAppSettings, MongoSettings):
    APP_NAME: str = "project-service"


class NotificationServiceSettings(BaseAppSettings, MongoSettings):
    APP_NAME: str = "notification-service"


class APIGatewaySettings(BaseAppSettings, ServiceSettings):
    APP_NAME: str = "api-gateway"