from fastapi import APIRouter, Depends

from use_case.auth_proxy import AuthProxyUseCase
from util.dependencies import get_auth_proxy_use_case

auth_proxy_router = APIRouter(prefix="/auth", tags=["proxy-auth"])


@auth_proxy_router.post("/register", summary="Proxy: register", description="Passes registration request to auth service.")
async def register(body: dict, use_case: AuthProxyUseCase = Depends(get_auth_proxy_use_case)):
    return await use_case.register(body)


@auth_proxy_router.post("/login", summary="Proxy: login", description="Passes login request to auth service.")
async def login(body: dict, use_case: AuthProxyUseCase = Depends(get_auth_proxy_use_case)):
    return await use_case.login(body)


@auth_proxy_router.post("/refresh", summary="Proxy: refresh token", description="Passes refresh request to auth service.")
async def refresh(body: dict, use_case: AuthProxyUseCase = Depends(get_auth_proxy_use_case)):
    return await use_case.refresh(body)
