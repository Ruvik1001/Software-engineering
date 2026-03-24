from collections.abc import Generator

from fastapi import Depends

from implementation.repository import InMemoryTaskRepository
from interface.repository import TaskRepository
from use_case.service import TaskService

_repo = InMemoryTaskRepository()


def get_task_repository() -> Generator[TaskRepository, None, None]:
    yield _repo


def get_task_service(repo: TaskRepository = Depends(get_task_repository)) -> TaskService:
    return TaskService(repo=repo)
