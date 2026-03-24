from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_mock_notification_endpoint():
    response = client.post("/api/v1/notification", json={"message": "test"})
    assert response.status_code == 200
