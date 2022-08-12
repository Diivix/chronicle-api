from fastapi import APIRouter

from ..db.database import db_create_user, db_get_user

from ..models.user import UserCreate, UserRead

router = APIRouter()

# Create new campaign
@router.post(path="/user", response_model=UserRead)
def create_user(user: UserCreate) -> UserRead:
    return db_create_user(user)


@router.get(path="/user/{id}", response_model=UserRead)
def get_user(id: int) -> UserRead:
    return db_get_user(id)
