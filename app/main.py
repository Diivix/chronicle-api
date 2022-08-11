import uvicorn
from typing import Union

from fastapi import FastAPI

from routers import journal

app = FastAPI()

app.include_router(journal.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)