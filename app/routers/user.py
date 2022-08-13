from fastapi import APIRouter, Depends
from sqlmodel import Session

from ..db.database import db_create_user, db_delete_user, db_get_user, get_db_session

from ..models.user import UserCreate, UserRead

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)
# Create new user
@router.post(path="/", response_model=UserRead)
def create_user(
    *, db_session: Session = Depends(get_db_session), user: UserCreate
) -> UserRead:
    return db_create_user(db_session, user)


@router.get(path="/{id}", response_model=UserRead)
def get_user(*, db_session: Session = Depends(get_db_session), id: int) -> UserRead:
    return db_get_user(db_session, id)


@router.delete(path="/{id}", response_model=str)
def delete_user(*, db_session: Session = Depends(get_db_session), id: int) -> str:
    if db_delete_user(db_session, id):
        return "User deleted"
    else:
        return "User not found or not deleted"
