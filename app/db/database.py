import os
from sqlmodel import create_engine

DATABASE_URL = os.environ.getenv('DATABASE_URL', '')
engine = create_engine(DATABASE_URL)
