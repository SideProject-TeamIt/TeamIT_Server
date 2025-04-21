from pydantic import BaseSettings


class Settings(BaseSettings):
    AUTH_SERVICE_URL: str = "http://auth-service:8000"
    USER_SERVICE_URL: str = "http://user-service:8000"
    TEAM_SERVICE_URL: str = "http://team-service:8000"
    PROJECT_SERVICE_URL: str = "http://project-service:8000"
    NOTIFICATION_SERVICE_URL: str = "http://notification-service:8000"

    # 추후 인증 관련 설정 추가될 수 있음

    class Config:
        env_file = ".env"


settings = Settings()