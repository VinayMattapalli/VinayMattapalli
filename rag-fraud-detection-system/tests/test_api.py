from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/")
    assert response.status_code == 200

def test_predict():
    response = client.post("/predict", json={"amount": 500})
    assert response.status_code == 200