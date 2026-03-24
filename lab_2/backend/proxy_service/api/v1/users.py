from fastapi import APIRouter, Depends

from use_case.user_proxy import UserProxyUseCase
from util.auth import get_token_value, require_user
from util.dependencies import get_user_proxy_use_case

user_proxy_router = APIRouter(prefix="/users", tags=["proxy-users"])


@user_proxy_router.post("", summary="Proxy: create user", description="Authorized route. Creates user in user service.")
async def create_user(body: dict, token: str = Depends(get_token_value), use_case: UserProxyUseCase = Depends(get_user_proxy_use_case)):
    await require_user(token)
    return await use_case.create_user(token=token, payload=body)


@user_proxy_router.get("/by-login/{login}", summary="Proxy: get user by login", description="Authorized route. Fetches one user profile.")
async def user_by_login(login: str, token: str = Depends(get_token_value), use_case: UserProxyUseCase = Depends(get_user_proxy_use_case)):
    await require_user(token)
    return await use_case.by_login(token=token, login=login)


@user_proxy_router.get("/search", summary="Proxy: search users", description="Authorized route. Finds users by name mask.")
async def user_search(mask: str, token: str = Depends(get_token_value), use_case: UserProxyUseCase = Depends(get_user_proxy_use_case)):
    await require_user(token)
    return await use_case.search(token=token, mask=mask)
