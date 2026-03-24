from pydantic import BaseModel, Field


class CreateUserRequest(BaseModel):
    login: str = Field(min_length=3, max_length=64)
    first_name: str = Field(min_length=1, max_length=64)
    last_name: str = Field(min_length=1, max_length=64)


class UserResponse(BaseModel):
    id: int
    login: str
    first_name: str
    last_name: str
