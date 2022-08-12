from fastapi import APIRouter

from ..db.database import db_create_user, db_delete_user, db_get_user

from ..models.user import UserCreate, UserRead

router = APIRouter()

# Create new user
@router.post(path="/user", response_model=UserRead)
def create_user(user: UserCreate) -> UserRead:
    return db_create_user(user)


@router.get(path="/user/{id}", response_model=UserRead)
def get_user(id: int) -> UserRead:
    return db_get_user(id)


@router.delete(path="/user/{id}", response_model=str)
def delete_user(id: int) -> str:
    if db_delete_user(id):
        return "User deleted"
    else:
        return "User not found or not deleted"
