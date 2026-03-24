from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_task_lifecycle() -> None:
    created = client.post("/api/v1/tasks", json={"goal_id": 1, "title": "Task 1", "assignee_login": "john"})
    assert created.status_code == 200
    task_id = created.json()["id"]

    listed = client.get("/api/v1/tasks/by-goal/1")
    assert listed.status_code == 200
    assert len(listed.json()) >= 1

    updated = client.patch(f"/api/v1/tasks/{task_id}/status", json={"status": "done"})
    assert updated.status_code == 200


def test_invalid_status_on_create() -> None:
    response = client.post("/api/v1/tasks", json={"goal_id": 1, "title": "T", "assignee_login": "john", "status": "bad"})
    assert response.status_code == 400


def test_update_missing_task() -> None:
    response = client.patch("/api/v1/tasks/9999/status", json={"status": "done"})
    assert response.status_code == 404
