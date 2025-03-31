from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "여기는 api-gateway 페이지입니다"}
