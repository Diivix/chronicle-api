from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

from .common import CommonBase


class UserBase(SQLModel):
    name: str
    email: str


class User(CommonBase, UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password_hash: Optional[str] = Field(default=None)

    campaigns: List["Campaign"] = Relationship(back_populates="user")  # type: ignore


class UserCreate(UserBase):
    password: str


class UserRead(CommonBase, UserBase):
    id: int
