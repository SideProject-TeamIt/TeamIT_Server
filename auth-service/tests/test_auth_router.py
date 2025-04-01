from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "여기는 auth_service 페이지입니다"}
