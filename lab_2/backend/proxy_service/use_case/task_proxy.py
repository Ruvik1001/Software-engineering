from use_case.proxy_client import ProxyGatewayUseCase
from util.config import TASK_URL


class TaskProxyUseCase:
    def __init__(self, gateway: ProxyGatewayUseCase) -> None:
        self._gateway = gateway

    async def create_task(self, token: str, payload: dict) -> dict | list:
        return await self._gateway.forward("POST", f"{TASK_URL}/api/v1/tasks", token=token, payload=payload)

    async def by_goal(self, token: str, goal_id: int) -> dict | list:
        return await self._gateway.forward("GET", f"{TASK_URL}/api/v1/tasks/by-goal/{goal_id}", token=token)

    async def update_status(self, token: str, task_id: int, payload: dict) -> dict | list:
        return await self._gateway.forward("PATCH", f"{TASK_URL}/api/v1/tasks/{task_id}/status", token=token, payload=payload)
