from pydantic import BaseModel


class ProxyAuthResponse(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str
