from pydantic import BaseModel
from app.schema.task_schema import Task


class UserBase(BaseModel):
    name: str


class User(UserBase):
    id: int
    tasks: list[Task] = []

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass
