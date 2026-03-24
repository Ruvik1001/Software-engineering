from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_mock_calendar_events():
    response = client.get("/api/v1/calendar/events")
    assert response.status_code == 200
