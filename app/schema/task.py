from pydantic import BaseModel


class TaskBase(BaseModel):
    name: str
    description: str
    status: str
    user_id: int

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
