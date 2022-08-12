from typing import Optional
from sqlmodel import Field, Relationship, SQLModel

from .campaign import Campaign
from .common import CommonBase


class JournalEntryBase(SQLModel):
    entry: str


class JournalEntry(CommonBase, JournalEntryBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    campaign_id: int = Field(default=None, foreign_key="campaign.id")
    campaign: Campaign = Relationship(back_populates="journal_entries")


class JournalEntryCreate(JournalEntryBase):
    pass


class JournalEntryRead(CommonBase, JournalEntryBase):
    id: int
