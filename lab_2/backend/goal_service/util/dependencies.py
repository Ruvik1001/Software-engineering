from collections.abc import Generator

from fastapi import Depends

from implementation.repository import InMemoryGoalRepository
from interface.repository import GoalRepository
from use_case.service import GoalService

_repo = InMemoryGoalRepository()


def get_goal_repository() -> Generator[GoalRepository, None, None]:
    yield _repo


def get_goal_service(repo: GoalRepository = Depends(get_goal_repository)) -> GoalService:
    return GoalService(repo=repo)
