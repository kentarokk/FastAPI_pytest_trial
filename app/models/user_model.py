from sqlmodel import SQLModel, Field, Relationship
from app.models.task_model import Task


class User(SQLModel, table=True):
    __tablename__ = 'users'

    id: int = Field(primary_key=True)
    name: str = Field(max_length=100)
    tasks: list["Task"] = Relationship(back_populates="user")
