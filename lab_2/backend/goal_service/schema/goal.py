from pydantic import BaseModel, Field


class CreateGoalRequest(BaseModel):
    title: str = Field(min_length=1, max_length=256)
    owner_login: str = Field(min_length=3, max_length=64)


class GoalResponse(BaseModel):
    id: int
    title: str
    owner_login: str
