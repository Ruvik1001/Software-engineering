from typing import Protocol

from model.user import AuthUser


class AuthRepository(Protocol):
    def create_user(self, user: AuthUser) -> AuthUser: ...

    def get_user(self, login: str) -> AuthUser | None: ...
