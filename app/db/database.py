import hashlib
from http.client import HTTPException
from typing import Any, List
from unittest import result
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


# TODO: Queries will need to change when auth is added.'
# E.g. only users should be able to CRUD their own data.

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
        return db_delete_entity(statement)


# Campaigns


def db_create_campaign(campaign: CampaignCreate, user: User) -> Campaign:
    with Session(engine) as session:
        db_campaign = Campaign.from_orm(campaign)
        db_campaign.user = user
        session.add(db_campaign)

        session.commit()
        session.refresh(db_campaign)
        return db_campaign


def db_get_campaign(id: int) -> Campaign:
    with Session(engine) as session:
        statement = select(Campaign).where(Campaign.id == id)
        result = session.exec(statement).one()
        return result


def db_get_all_user_campaigns(user: User) -> List[Campaign]:
    with Session(engine) as session:
        statement = select(Campaign).where(Campaign.user_id == user.id)
        results = session.exec(statement).all()
        return results


def db_delete_campaign(id: int) -> bool:
    with Session(engine) as session:
        statement = select(Campaign).where(Campaign.id == id)
        return db_delete_entity(statement)


# Journal Entries


def db_create_journal_entry(
    entry: JournalEntryCreate, campaign: CampaignCreate
) -> JournalEntry:
    with Session(engine) as session:
        db_entry = JournalEntry.from_orm(entry)
        db_entry.campaign = campaign
        session.add(db_entry)

        session.commit()
        session.refresh(db_entry)
        return db_entry


def db_get_journal_entry(id: int) -> JournalEntry:
    with Session(engine) as session:
        statement = select(JournalEntry).where(JournalEntry.id == id)
        result = session.exec(statement).one()
        return result


def db_get_all_campaign_journal_entries(campaign: Campaign) -> List[JournalEntry]:
    with Session(engine) as session:
        statement = select(JournalEntry).where(JournalEntry.campaign_id == campaign.id)
        results = session.exec(statement).all()
        return results


def db_delete_journal_entry(id: int) -> bool:
    with Session(engine) as session:
        statement = select(JournalEntry).where(JournalEntry.id == id)
        return db_delete_entity(statement)


# Common


def db_delete_entity(statement) -> bool:
    with Session(engine) as session:
        result = session.exec(statement).first()
        if result is None:
            return False

        session.delete(result)
        session.commit()

        # Check it has been deleted
        result = session.exec(statement).first()
        return result is None


# TODO: Fix this so it works with package imports.
if __name__ == "__main__":
    db_init()
    print("DB initialized")
