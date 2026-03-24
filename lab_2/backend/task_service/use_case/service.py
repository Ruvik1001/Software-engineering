from interface.repository import TaskRepository


class TaskService:
    def __init__(self, repo: TaskRepository) -> None:
        self._repo = repo

    def create_task(self, data: dict) -> dict:
        return self._repo.create(**data).__dict__

    def get_tasks(self, goal_id: int) -> list[dict]:
        return [t.__dict__ for t in self._repo.by_goal(goal_id)]

    def update_status(self, task_id: int, status: str) -> dict | None:
        task = self._repo.set_status(task_id, status)
        return task.__dict__ if task else None
