from fastapi import FastAPI

from .routers import journal, user

app = FastAPI()


@app.get("/")
def index():
    return "Chronicle online."


@app.get("/health")
def index():
    return "healthy"


app.include_router(journal.router)
app.include_router(user.router)
