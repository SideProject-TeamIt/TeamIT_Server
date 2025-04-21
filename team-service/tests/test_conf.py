import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    """테스트 클라이언트 픽스처"""
    with TestClient(app) as test_client:
        yield test_client