from fastapi import FastAPI
from shared.database.postgres import Base, engine
import app.models.user  # 모델 import 필수

app = FastAPI()

# 테이블 자동 생성
Base.metadata.create_all(bind=engine)
