from typing import List
from sqlmodel import Session, SQLModel, create_engine, select

from ..models.user import User, UserRead
from ..models.campaign import Campaign, CampaignRead

sqlite_file_name = "data/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def db_init():
    """Create db and tables if they don't exist."""
    SQLModel.metadata.create_all(engine)


# Users


def db_create_user(user: User) -> UserRead:
    with Session(engine) as session:
        db_user = User.from_orm(user)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user


def db_get_user(user_id: int) -> UserRead:
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        user = session.execute(statement).one()
        return user


# Campaigns


def db_create_campaign(campaign: Campaign, user: UserRead) -> CampaignRead:
    with Session(engine) as session:
        db_campaign = Campaign.from_orm(campaign)
        db_campaign.user = user

        session.add(db_campaign)
        session.commit()
        session.refresh(db_campaign)
        return db_campaign


def db_get_campaign(id: int) -> CampaignRead:
    with Session(engine) as session:
        statement = select(Campaign).where(Campaign.id == id)
        results = session.execute(statement)
        return results.one()


def db_get_all_campaigns() -> List[CampaignRead]:
    with Session(engine) as session:
        statement = select(Campaign)
        results = session.execute(statement).all()
        return results


def db_deactivate_campaign(id: int) -> bool:
    with Session(engine) as session:
        statement = select(Campaign).where(Campaign.id == id)
        results = session.execute(statement)
        campaign = results.one()

        session.delete(campaign)
        session.commit()

        results = session.execute(statement)
        campaigns = results.first()

        if campaign is not None:
            print("Campaign not not deactivated")
            return False
