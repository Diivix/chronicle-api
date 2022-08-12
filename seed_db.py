from app.models.campaign import Campaign, CampaignCreate
from app.models.journal_entry import JournalEntry, JournalEntryCreate
from app.models.user import User, UserCreate
from app.db.database import (
    db_create_campaign,
    db_init,
    db_create_user,
    db_create_journal_entry,
)


def init_db():
    print("Initializing database")
    db_init()


# Create seeded user
def create_user() -> User:
    print("Creating seeded user")
    user = UserCreate(name="Diivix", email="diivix@chronicle.com", password="password")
    db_user = db_create_user(user)
    print(db_user)
    return db_user


# Create seeded user
def create_campaign(user: UserCreate) -> Campaign:
    print("Creating seeded campaign")

    campaign = CampaignCreate(
        name="My Campaign",
        description="A simple campaign",
    )
    db_campaign = db_create_campaign(campaign, user)
    print(db_campaign)
    return db_campaign


def create_journal_entry(campaign_id: int, user: User) -> JournalEntry:
    print("Creating seeded journal entry")

    journal_entry = JournalEntryCreate(entry="My first journal entry")
    db_journal_entry = db_create_journal_entry(journal_entry, campaign_id, user)
    print(db_journal_entry)
    return db_journal_entry


if __name__ == "__main__":
    init_db()
    user = create_user()
    campaign = create_campaign(user)
    entry = create_journal_entry(campaign.id, user)
