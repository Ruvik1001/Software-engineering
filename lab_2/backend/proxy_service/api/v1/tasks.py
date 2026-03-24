from fastapi import APIRouter, Depends

from use_case.task_proxy import TaskProxyUseCase
from util.auth import get_token_value, require_user
from util.dependencies import get_task_proxy_use_case

task_proxy_router = APIRouter(prefix="/tasks", tags=["proxy-tasks"])


@task_proxy_router.post("", summary="Proxy: create task", description="Authorized route. Creates task in task service.")
async def create_task(body: dict, token: str = Depends(get_token_value), use_case: TaskProxyUseCase = Depends(get_task_proxy_use_case)):
    await require_user(token)
    return await use_case.create_task(token=token, payload=body)


@task_proxy_router.get("/by-goal/{goal_id}", summary="Proxy: list goal tasks", description="Authorized route. Returns tasks for selected goal.")
async def tasks_by_goal(goal_id: int, token: str = Depends(get_token_value), use_case: TaskProxyUseCase = Depends(get_task_proxy_use_case)):
    await require_user(token)
    return await use_case.by_goal(token=token, goal_id=goal_id)


@task_proxy_router.patch("/{task_id}/status", summary="Proxy: update task status", description="Authorized route. Updates task status in task service.")
async def task_status(task_id: int, body: dict, token: str = Depends(get_token_value), use_case: TaskProxyUseCase = Depends(get_task_proxy_use_case)):
    await require_user(token)
    return await use_case.update_status(token=token, task_id=task_id, payload=body)
