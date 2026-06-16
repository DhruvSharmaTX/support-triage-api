from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
def test_invalid_payload():
    payload = {"title": ""}
    response = client.post("/tickets/analyze", json=payload)
    assert response.status_code == 422
