from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "여기는 user-service 페이지입니다"}
