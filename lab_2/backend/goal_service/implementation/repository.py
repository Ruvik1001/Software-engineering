from model.goal import Goal


class InMemoryGoalRepository:
    def __init__(self) -> None:
        self._seq = 1
        self._goals: dict[int, Goal] = {}

    def create(self, title: str, owner_login: str) -> Goal:
        goal = Goal(id=self._seq, title=title, owner_login=owner_login)
        self._goals[self._seq] = goal
        self._seq += 1
        return goal

    def list_all(self) -> list[Goal]:
        return list(self._goals.values())
