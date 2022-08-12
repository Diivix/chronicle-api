from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

from .common import CommonBase


class UserBase(SQLModel):
    name: str
    email: str
    password_hash: str


class User(CommonBase, UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    campaigns: List["Campaign"] = Relationship(back_populates="user")


class UserCreate(UserBase):
    pass


class UserRead(CommonBase, UserBase):
    id: int
