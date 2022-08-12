import hashlib
from datetime import datetime
from fastapi import APIRouter

from ..db.db import db_create_user, db_get_user

from ..models.user import User, UserCreate, UserRead

router = APIRouter()

# Create new campaign
@router.post("/user")
def create_user(user: UserCreate) -> UserRead:
    return db_create_user(user)


@router.get("/user/{id}")
def get_user(id: int) -> UserRead:
    return db_get_user(id)
