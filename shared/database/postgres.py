from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_postgres_engine(db_url: str):
    return create_engine(db_url, echo=True)

def get_postgres_session(engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)
