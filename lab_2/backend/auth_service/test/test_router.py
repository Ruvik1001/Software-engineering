from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_register_and_login_success() -> None:
    register = client.post(
        "/api/v1/auth/register",
        json={"login": "owner", "password": "pass123", "first_name": "Own", "last_name": "Er"},
    )
    assert register.status_code == 200

    login = client.post("/api/v1/auth/login", json={"login": "owner", "password": "pass123"})
    assert login.status_code == 200
    assert "access_token" in login.json()


def test_register_duplicate_login() -> None:
    client.post("/api/v1/auth/register", json={"login": "dup", "password": "pass", "first_name": "A", "last_name": "B"})
    duplicate = client.post("/api/v1/auth/register", json={"login": "dup", "password": "pass", "first_name": "A", "last_name": "B"})
    assert duplicate.status_code == 400


def test_refresh_with_access_token_fails() -> None:
    client.post(
        "/api/v1/auth/register",
        json={"login": "r1_refresh", "password": "pass", "first_name": "A", "last_name": "B"},
    )
    login = client.post("/api/v1/auth/login", json={"login": "r1_refresh", "password": "pass"})
    assert login.status_code == 200
    bad = client.post("/api/v1/auth/refresh", json={"refresh_token": login.json()["access_token"]})
    assert bad.status_code == 401
