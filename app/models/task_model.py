from typing import Optional, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.user_model import User


class Task(SQLModel, table=True):
    __tablename__ = 'tasks'

    id: int = Field(primary_key=True)
    name: str = Field(max_length=100)
    description: str = Field(max_length=100)
    status: str = Field(max_length=100)
    user_id: int = Field(foreign_key="users.id")

    user: Optional["User"] = Relationship(back_populates="tasks")
