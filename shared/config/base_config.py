import os
from dotenv import load_dotenv

load_dotenv()

class BaseConfig:
    # PostgreSQL
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

    @classmethod
    def get_postgres_url(cls):
        return (
            f"postgresql://{cls.POSTGRES_USER}:{cls.POSTGRES_PASSWORD}"
            f"@{cls.POSTGRES_HOST}:{cls.POSTGRES_PORT}/{cls.POSTGRES_DB}"
        )

    # MongoDB
    MONGO_DB = os.getenv("MONGO_DB")
    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT = os.getenv("MONGO_PORT", "27017")

    @classmethod
    def get_mongo_uri(cls):
        return f"mongodb://{cls.MONGO_HOST}:{cls.MONGO_PORT}/{cls.MONGO_DB}"
