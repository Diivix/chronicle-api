from datetime import datetime
from fastapi import APIRouter

from ..db.db import db_create_user

from ..models.user import User, UserCreate

router = APIRouter()

# Create new campaign
@router.post("/user")
def create_user(user: UserCreate) -> User:
    user_user = User(**user.dict())
    now = datetime.now().isoformat()
    user_user.created = now
    user_user.updated = now
    db_create_user(user_user)
    return user