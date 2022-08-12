from typing import Optional
from sqlmodel import Field, SQLModel

from .common import CommonBase


class CampaignBase(SQLModel):
    name: str = Field(index=True)
    description: str


class Campaign(CommonBase, CampaignBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class CampaignCreate(CampaignBase):
    pass


class CampaignRead(CommonBase, CampaignBase):
    id: int
