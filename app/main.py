from fastapi import FastAPI

from .db.db import db_init
from .routers import journal, user

db_init()
app = FastAPI()


@app.get("/")
def index():
    return "Chronicle online."


@app.get("/health")
def index():
    return "healthy"


app.include_router(journal.router)
app.include_router(user.router)
