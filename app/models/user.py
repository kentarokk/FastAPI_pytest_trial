from sqlmodel import SQLModel, Field, relationship

class User(SQLModel, table=True):
    __tablename__ = 'users'

    id: int = Field(primary_key=True)
    name: str = Field(max_length=100)
    tasks = relationship("Task", back_populates="user")

