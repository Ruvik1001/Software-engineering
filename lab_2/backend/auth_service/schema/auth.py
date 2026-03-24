from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):
    login: str = Field(min_length=3, max_length=64, examples=["john"])
    password: str = Field(min_length=4, max_length=128, examples=["qwerty"])
    first_name: str = Field(min_length=1, max_length=64, examples=["John"])
    last_name: str = Field(min_length=1, max_length=64, examples=["Doe"])


class RegisterResponse(BaseModel):
    login: str
    first_name: str
    last_name: str


class LoginRequest(BaseModel):
    login: str
    password: str


class RefreshRequest(BaseModel):
    refresh_token: str


class ValidateRequest(BaseModel):
    token: str


class TokenPairResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class AccessTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ValidateResponse(BaseModel):
    login: str
