from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_protected_endpoint_requires_token() -> None:
    response = client.get("/api/v1/goals")
    assert response.status_code == 401


def test_protected_endpoint_rejects_bad_header() -> None:
    response = client.get("/api/v1/goals", headers={"Authorization": "Basic abc"})
    assert response.status_code == 401
