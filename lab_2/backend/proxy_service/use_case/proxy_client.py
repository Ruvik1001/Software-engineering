from fastapi import HTTPException
import httpx


class ProxyGatewayUseCase:
    async def forward(
        self,
        method: str,
        url: str,
        token: str | None = None,
        payload: dict | None = None,
    ) -> dict | list:
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"

        async with httpx.AsyncClient(timeout=5) as client:
            if method == "GET":
                resp = await client.request(method, url, headers=headers, params=payload)
            else:
                resp = await client.request(method, url, headers=headers, json=payload)

        if resp.status_code >= 400:
            raise HTTPException(status_code=resp.status_code, detail=resp.text)

        if not resp.text:
            return {}
        return resp.json()
