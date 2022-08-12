from typing import Optional
from sqlmodel import Field, SQLModel

from .common import CommonBase


class JournalEntryBase(SQLModel):
    entry: str


class JournalEntry(CommonBase, JournalEntryBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class JournalEntryCreate(JournalEntryBase):
    pass


class JournalEntryRead(CommonBase, JournalEntryBase):
    id: int
