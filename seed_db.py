from sqlmodel import Session

from app.models.campaign import Campaign, CampaignCreate
from app.models.journal_entry import JournalEntry, JournalEntryCreate
from app.models.user import User, UserCreate
from app.db.database import (
    db_create_campaign,
    get_db_session,
    init_db,
    db_create_user,
    db_create_journal_entry,
)


# Create seeded user
def create_user(session: Session) -> User:
    print("Creating seeded user")
    user = UserCreate(name="Diivix", email="diivix@chronicle.com", password="password")
    db_user = db_create_user(session, user)
    print(db_user)
    return db_user


# Create seeded user
def create_campaign(session: Session, user: UserCreate) -> Campaign:
    print("Creating seeded campaign")

    campaign = CampaignCreate(
        name="My Campaign",
        description="A simple campaign",
    )
    db_campaign = db_create_campaign(session, campaign, user)
    print(db_campaign)
    return db_campaign


def create_journal_entry(
    session: Session, campaign_id: int, user: User
) -> JournalEntry:
    print("Creating seeded journal entry")

    journal_entry = JournalEntryCreate(entry="My first journal entry")
    db_journal_entry = db_create_journal_entry(
        session, journal_entry, campaign_id, user
    )
    print(db_journal_entry)
    return db_journal_entry


if __name__ == "__main__":
    init_db()
    session = next(get_db_session())
    
    user = create_user(session)
    campaign = create_campaign(session, user)
    entry = create_journal_entry(session, campaign.id, user)
