import hashlib
from typing import List
from sqlmodel import Session, create_engine, select

from ..models.user import User, UserCreate
from ..models.campaign import Campaign, CampaignCreate
from ..models.journal_entry import JournalEntry, JournalEntryCreate

sqlite_file_name = "data/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
mssql_url = "mssql+pyodbc://sa:StrongP^ssword@localhost:1433/chronicle?driver=ODBC+Driver+17+for+SQL+Server"

connect_args = {"check_same_thread": False}
engine = create_engine(
    mssql_url, echo=True, connect_args=connect_args
).execution_options(autocommit=True)


def get_db_session():
    with Session(engine) as session:
        yield session


# TODO: Queries will need to change when auth is added.'
# E.g. only users should be able to CRUD their own data.

# Users
# TODO: Lock down access to users.


def db_create_user(session: Session, user: UserCreate) -> User:
    db_user = User.from_orm(user)
    db_user.password_hash = hashlib.md5(user.password.encode("utf_8")).hexdigest()

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def db_get_user(session: Session, user_id: int) -> User:
    statement = select(User).where(User.id == user_id)
    user = session.exec(statement).one()
    return user


def db_delete_user(session: Session, id: int) -> bool:
    statement = select(User).where(User.id == id)
    return db_delete_entity(session, statement)


# Campaigns


def db_create_campaign(
    session: Session, campaign: CampaignCreate, user: User
) -> Campaign:
    db_campaign = Campaign.from_orm(campaign)
    db_campaign.user = user
    session.add(db_campaign)

    session.commit()
    session.refresh(db_campaign)
    return db_campaign


def db_get_campaign(session: Session, id: int, user: User) -> Campaign:
    statement = select(Campaign).where(Campaign.id == id, Campaign.user_id == user.id)
    result = session.exec(statement).first()
    return result


def db_get_all_user_campaigns(session: Session, user: User) -> List[Campaign]:
    statement = select(Campaign).where(Campaign.user_id == user.id)
    results = session.exec(statement).all()
    return results


def db_delete_campaign(session: Session, id: int, user: User) -> bool:
    statement = select(Campaign).where(Campaign.id == id, Campaign.user_id == user.id)
    return db_delete_entity(session, statement)


# Journal Entries


def db_create_journal_entry(
    session: Session, entry: JournalEntryCreate, campaign_id: int, user: User
) -> JournalEntry:
    session.add(user)

    db_campaign = db_get_campaign(session, campaign_id, user)
    db_entry = JournalEntry.from_orm(entry)
    db_entry.campaign = db_campaign
    session.add(db_entry)

    session.commit()
    session.refresh(db_entry)
    return db_entry


def db_get_journal_entry(session: Session, entry_id: int, user: User) -> JournalEntry:
    statement = (
        select(JournalEntry)
        .join(Campaign)
        .where(
            JournalEntry.id == entry_id,
            Campaign.id == JournalEntry.campaign_id,
            Campaign.user_id == user.id,
        )
    )
    result = session.exec(statement).first()
    return result


def db_get_campaign_journal_entries(
    session: Session, campaign_id: int, user: User
) -> List[JournalEntry]:
    statement = (
        select(JournalEntry)
        .join(Campaign)
        .where(
            Campaign.id == campaign_id,
            Campaign.id == JournalEntry.campaign_id,
            Campaign.user_id == user.id,
        )
    )

    results = session.exec(statement).all()
    return results


def db_delete_journal_entry(session: Session, id: int) -> bool:
    statement = select(JournalEntry).where(JournalEntry.id == id)
    return db_delete_entity(session, statement)


# Common DB actions


def db_delete_entity(session: Session, statement) -> bool:
    """Delete an entity from the database"""
    result = session.exec(statement).first()
    if result is None:
        return False

    session.delete(result)
    session.commit()

    # Check it has been deleted
    result = session.exec(statement).first()
    return result is None
