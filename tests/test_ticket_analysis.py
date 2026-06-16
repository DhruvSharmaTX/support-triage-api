from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
def test_ticket_analysis():
    payload = {
        "title": "Cannot access admin page",
        "description": "Permission denied while opening settings",
        "channel": "Email",
        "requester_type": "Customer",
    }
    response = client.post("/tickets/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "predicted_category" in data
    assert "predicted_priority" in data
