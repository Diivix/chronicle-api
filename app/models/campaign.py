from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

from .common import CommonBase
from .user import User


class CampaignBase(SQLModel):
    name: str
    description: str


class Campaign(CommonBase, CampaignBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: int = Field(default=None, foreign_key="user.id")
    user: User = Relationship(back_populates="campaigns")

    journal_entries: List["JournalEntry"] = Relationship(back_populates="campaign", sa_relationship_kwargs={"cascade": "all, delete"})  # type: ignore


class CampaignCreate(CampaignBase):
    pass


class CampaignRead(CommonBase, CampaignBase):
    id: int
