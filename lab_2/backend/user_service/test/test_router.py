from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_and_get_user() -> None:
    created = client.post("/api/v1/users", json={"login": "john", "first_name": "John", "last_name": "Doe"})
    assert created.status_code == 200

    fetched = client.get("/api/v1/users/by-login/john")
    assert fetched.status_code == 200
    assert fetched.json()["first_name"] == "John"


def test_user_not_found() -> None:
    response = client.get("/api/v1/users/by-login/unknown")
    assert response.status_code == 404


def test_create_duplicate_user() -> None:
    client.post("/api/v1/users", json={"login": "dup_user", "first_name": "A", "last_name": "B"})
    duplicate = client.post("/api/v1/users", json={"login": "dup_user", "first_name": "A", "last_name": "B"})
    assert duplicate.status_code == 400
