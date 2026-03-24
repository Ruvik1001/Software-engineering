from pydantic import BaseModel, Field


class CreateTaskRequest(BaseModel):
    goal_id: int
    title: str = Field(min_length=1, max_length=256)
    assignee_login: str = Field(min_length=3, max_length=64)
    status: str = "new"


class UpdateStatusRequest(BaseModel):
    status: str


class TaskResponse(BaseModel):
    id: int
    goal_id: int
    title: str
    assignee_login: str
    status: str
