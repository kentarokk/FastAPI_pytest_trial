from fastapi import FastAPI
from app.router import main_router

api = FastAPI()

api.include_router(main_router.router, tags=["main"])
