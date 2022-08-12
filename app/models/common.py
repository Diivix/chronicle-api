from datetime import datetime
from sqlmodel import Field, SQLModel


class CommonBase(SQLModel):
    created: datetime
    updated: datetime
    is_active: bool = Field(default=True)
