from dataclasses import dataclass


@dataclass
class Task:
    id: int
    goal_id: int
    title: str
    assignee_login: str
    status: str
