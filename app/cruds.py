from sqlalchemy.orm import Session
from app.models import user_model, task_model
from app.schema import user_schema, task_schema


def get_user(db: Session, user_id: int):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()


def get_user_by_name(db: Session, user_name: str):
    return db.query(user_model.User).filter(user_model.User.name == user_name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schema.UserBase):
    new_user = user_model.User(name=user.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(user_model.Task).filter(task_model.Task.user_id == user_id).offset(skip).limit(limit).all()


def create_task(db: Session, task: task_schema.TaskCreate, user_id: int):
    new_task = task_model.Task(**task.dict(), user_id=user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
