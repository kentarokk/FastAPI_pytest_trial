from sqlmodel import SQLModel, Field

class Task(SQLModel, table=True):
    __tablename__ = 'tasks'

    id: int = Field(primary_key=True)
    name: str = Field(max_length=100)
    description: str = Field(max_length=100)
    status: str = Field(max_length=100)
    user_id: int = Field(foreign_key="users.id")
