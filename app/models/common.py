from datetime import datetime
from sqlmodel import Field, SQLModel


class CommonBase(SQLModel):
    created: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    # is_active: bool = Field(default=True, nullable=False)
