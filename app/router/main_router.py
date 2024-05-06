from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import cruds
from app.schema import user_schema
from app.db.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def index():
    return {"msg": "Hello, World!"}


@router.post("/user", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db_session: Session = Depends(get_db)):
    db_user = cruds.get_user_by_name(db_session, user_name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail=f"User name: {user.name} already exists.")
    return cruds.create_user(db_session, user=user)


@router.get("/user/{user_id}", response_model=user_schema.User)
def get_user(user_id: int, db_session: Session = Depends(get_db)):
    user = cruds.get_user(db_session, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User ID: {user_id} not found")
    return user
