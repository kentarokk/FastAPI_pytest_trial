from fastapi import FastAPI
from app.router import main_router

app = FastAPI()

app.include_router(main_router.router, tags=["main"])
