from sqlalchemy.orm import Session
from app.models import user_model
from app.schema import user_schema


def get_user(db: Session, user_id: int):
    # return db.query(user.User).filter(user.User.id == user_id).first()
    return 123


def get_user_by_name(db: Session, user_name: str):
    # return db.query(user.User).filter(user.User.name == user_name).first()
    return 123


def create_user(db: Session, user: user_schema.UserBase):
    new_user = user_model.User(name=user.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
