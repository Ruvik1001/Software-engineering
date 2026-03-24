from interface.repository import GoalRepository


class GoalService:
    def __init__(self, repo: GoalRepository) -> None:
        self._repo = repo

    def create_goal(self, data: dict) -> dict:
        return self._repo.create(**data).__dict__

    def list_goals(self) -> list[dict]:
        return [g.__dict__ for g in self._repo.list_all()]
