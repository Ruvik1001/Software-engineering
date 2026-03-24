from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_and_list_goals() -> None:
    created = client.post("/api/v1/goals", json={"title": "Learn FastAPI", "owner_login": "john"})
    assert created.status_code == 200

    listed = client.get("/api/v1/goals")
    assert listed.status_code == 200
    assert any(goal["title"] == "Learn FastAPI" for goal in listed.json())


def test_create_goal_validation_error() -> None:
    response = client.post("/api/v1/goals", json={"title": "", "owner_login": "john"})
    assert response.status_code == 422
