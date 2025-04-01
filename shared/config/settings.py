from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    MONGO_DB: str = "admin"
    MONGO_HOST: str = "localhost"
    MONGO_PORT: int = 27017

    class Config:
        env_file = ".env"  # 각 서비스 루트에서 .env 파일 자동 로딩

    @property
    def postgres_uri(self):
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    @property
    def mongo_uri(self):
        return f"mongodb://{self.MONGO_HOST}:{self.MONGO_PORT}"

settings = Settings()
