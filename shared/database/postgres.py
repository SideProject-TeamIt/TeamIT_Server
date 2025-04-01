from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from shared.config.settings import settings

engine = create_engine(settings.postgres_uri, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
