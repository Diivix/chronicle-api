import hashlib
from typing import List
from sqlmodel import Session, SQLModel, create_engine, select

from ..models.user import User, UserCreate
from ..models.campaign import Campaign, CampaignCreate
from ..models.journal_entry import JournalEntry, JournalEntryCreate

sqlite_file_name = "data/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def db_init():
    """Create db and tables if they don't exist."""
    SQLModel.metadata.create_all(engine)


# Users


def db_create_user(user: UserCreate) -> User:
    with Session(engine) as session:
        db_user = User.from_orm(user)
        db_user.password_hash = hashlib.md5(user.password.encode("utf_8")).hexdigest()

        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user


def db_get_user(user_id: int) -> User:
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).one()
        return user

def db_delete_user(id: int) -> bool:
    with Session(engine) as session:
        statement = select(User).where(User.id == id)
        user = session.exec(statement).one()

        session.delete(user)
        session.commit()

        user = session.exec(statement).first()
        return user is None

# Campaigns


def db_create_campaign(campaign: CampaignCreate, user: User) -> Campaign:
    with Session(engine) as session:
        db_campaign = Campaign.from_orm(campaign)
        db_campaign.user = user
        session.add(db_campaign)
        # session.add(user)

        session.commit()
        session.refresh(db_campaign)
        return db_campaign


def db_get_campaign(id: int) -> Campaign:
    with Session(engine) as session:
        statement = select(Campaign).where(Campaign.id == id)
        results = session.exec(statement)
        return results.one()


def db_get_all_campaigns() -> List[Campaign]:
    with Session(engine) as session:
        statement = select(Campaign)
        results = session.exec(statement).all()
        return results


def db_delete_campaign(id: int) -> bool:
    with Session(engine) as session:
        statement = select(Campaign).where(Campaign.id == id)
        campaign = session.exec(statement).one()

        session.delete(campaign)
        session.commit()

        campaign = session.exec(statement).first()

        return campaign is None


# TODO: Fix this so it works with package imports.
if __name__ == "__main__":
    db_init()
    print("DB initialized")
