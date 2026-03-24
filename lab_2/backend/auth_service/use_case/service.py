from interface.repository import AuthRepository
from model.user import AuthUser
from util.security import decode_token, encode_token


class AuthService:
    def __init__(self, repo: AuthRepository) -> None:
        self._repo = repo

    def register(self, data: dict) -> dict:
        created = self._repo.create_user(AuthUser(**data))
        return {"login": created.login, "first_name": created.first_name, "last_name": created.last_name}

    def login(self, login_value: str, password: str) -> dict:
        user = self._repo.get_user(login_value)
        if not user or user.password != password:
            raise ValueError("invalid credentials")
        access_token = encode_token({"sub": user.login}, expires_minutes=30)
        refresh_token = encode_token({"sub": user.login, "kind": "refresh"}, expires_minutes=60 * 24)
        return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

    def refresh(self, token: str) -> dict:
        payload = decode_token(token)
        if payload.get("kind") != "refresh":
            raise ValueError("invalid refresh token")
        access_token = encode_token({"sub": payload["sub"]}, expires_minutes=30)
        return {"access_token": access_token, "token_type": "bearer"}

    def validate(self, token: str) -> dict:
        payload = decode_token(token)
        return {"login": payload.get("sub")}
