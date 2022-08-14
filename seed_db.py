from sqlmodel import Session, create_engine, SQLModel
from sqlalchemy_utils import create_database, database_exists, drop_database

from app.models.campaign import Campaign, CampaignCreate
from app.models.journal_entry import JournalEntry, JournalEntryCreate
from app.models.user import User, UserCreate
from app.db.database import (
    db_create_campaign,
    db_create_user,
    db_create_journal_entry,
)

sqlite_file_name = "data/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

mssql_database_name = "chronicle"
mssql_url = f"mssql+pyodbc://sa:StrongP^ssword@localhost:1433/chronicle?driver=ODBC+Driver+17+for+SQL+Server"

connect_args = {"check_same_thread": False}
engine = create_engine(
    mssql_url, echo=True, connect_args=connect_args
).execution_options(autocommit=True)

def init_db():
    if database_exists(engine.url):
        drop_database(engine.url)

    create_database(engine.url)
    SQLModel.metadata.create_all(engine)

# Create seeded user
def create_user() -> User:
    with Session(engine) as session:
        print("Creating seeded user")
        user = UserCreate(
            name="Diivix", email="diivix@chronicle.com", password="password"
        )
        db_user = db_create_user(session, user)
        print(db_user)
        return db_user


# Create seeded user
def create_campaign(user: UserCreate) -> Campaign:
    with Session(engine) as session:
        print("Creating seeded campaign")

        campaign = CampaignCreate(
            name="My Campaign",
            description="A simple campaign",
        )
        db_campaign = db_create_campaign(session, campaign, user)
        print(db_campaign)
        return db_campaign


def create_journal_entry(campaign_id: int, user: User) -> JournalEntry:
    with Session(engine) as session:
        print("Creating seeded journal entry")

        journal_entry = JournalEntryCreate(entry="My first journal entry")
        db_journal_entry = db_create_journal_entry(
            session, journal_entry, campaign_id, user
        )
        print(db_journal_entry)
        return db_journal_entry


if __name__ == "__main__":
    init_db()

    user = create_user()
    campaign = create_campaign(user)
    entry = create_journal_entry(campaign.id, user)
