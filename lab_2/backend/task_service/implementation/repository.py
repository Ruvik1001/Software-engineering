from model.task import Task

ALLOWED_STATUSES = {"new", "in_progress", "done"}


class InMemoryTaskRepository:
    def __init__(self) -> None:
        self._seq = 1
        self._tasks: dict[int, Task] = {}

    def create(self, goal_id: int, title: str, assignee_login: str, status: str = "new") -> Task:
        if status not in ALLOWED_STATUSES:
            raise ValueError("invalid status")
        task = Task(id=self._seq, goal_id=goal_id, title=title, assignee_login=assignee_login, status=status)
        self._tasks[self._seq] = task
        self._seq += 1
        return task

    def by_goal(self, goal_id: int) -> list[Task]:
        return [t for t in self._tasks.values() if t.goal_id == goal_id]

    def set_status(self, task_id: int, status: str) -> Task | None:
        if status not in ALLOWED_STATUSES:
            raise ValueError("invalid status")
        task = self._tasks.get(task_id)
        if not task:
            return None
        task.status = status
        return task
