import os
from sqlmodel import create_engine
from sqlmodel.orm import Session, sessionmaker

DATABASE_URL = os.environ.getenv('DATABASE_URL', '')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
