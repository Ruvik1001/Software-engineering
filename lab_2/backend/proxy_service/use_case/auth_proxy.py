from use_case.proxy_client import ProxyGatewayUseCase
from util.config import AUTH_URL


class AuthProxyUseCase:
    def __init__(self, gateway: ProxyGatewayUseCase) -> None:
        self._gateway = gateway

    async def register(self, payload: dict) -> dict | list:
        return await self._gateway.forward("POST", f"{AUTH_URL}/api/v1/auth/register", payload=payload)

    async def login(self, payload: dict) -> dict | list:
        return await self._gateway.forward("POST", f"{AUTH_URL}/api/v1/auth/login", payload=payload)

    async def refresh(self, payload: dict) -> dict | list:
        return await self._gateway.forward("POST", f"{AUTH_URL}/api/v1/auth/refresh", payload=payload)
