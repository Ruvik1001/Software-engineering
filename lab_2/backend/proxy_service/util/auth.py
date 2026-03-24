from fastapi import Header, HTTPException
import httpx
from util.config import AUTH_URL

def get_token_value(authorization: str | None = Header(default=None)) -> str:
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="missing bearer token")
    return authorization.split(" ", maxsplit=1)[1]

async def require_user(token: str) -> str:
    async with httpx.AsyncClient(timeout=5) as client:
        resp = await client.post(f"{AUTH_URL}/api/v1/auth/validate", json={"token": token})
    if resp.status_code != 200:
        raise HTTPException(status_code=401, detail="invalid token")
    return resp.json()["login"]
