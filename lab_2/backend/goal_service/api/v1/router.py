from fastapi import APIRouter, Depends

from schema.goal import CreateGoalRequest, GoalResponse
from use_case.service import GoalService
from util.dependencies import get_goal_service

goal_router = APIRouter(tags=["goals"])


@goal_router.post(
    "/goals",
    response_model=GoalResponse,
    summary="Create goal",
    description="Creates a planning goal for an executor.",
)
def create(req: CreateGoalRequest, service: GoalService = Depends(get_goal_service)) -> GoalResponse:
    return GoalResponse.model_validate(service.create_goal(req.model_dump()))


@goal_router.get(
    "/goals",
    response_model=list[GoalResponse],
    summary="List goals",
    description="Returns all goals currently stored in memory.",
)
def list_all(service: GoalService = Depends(get_goal_service)) -> list[GoalResponse]:
    return [GoalResponse.model_validate(item) for item in service.list_goals()]
