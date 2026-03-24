from typing import Protocol

from model.goal import Goal


class GoalRepository(Protocol):
    def create(self, title: str, owner_login: str) -> Goal: ...

    def list_all(self) -> list[Goal]: ...
