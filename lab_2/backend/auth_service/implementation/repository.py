from model.user import AuthUser


class InMemoryAuthRepository:
    def __init__(self) -> None:
        self._users: dict[str, AuthUser] = {}

    def create_user(self, user: AuthUser) -> AuthUser:
        if user.login in self._users:
            raise ValueError("login already exists")
        self._users[user.login] = user
        return user

    def get_user(self, login: str) -> AuthUser | None:
        return self._users.get(login)
