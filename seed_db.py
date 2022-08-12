from app.models.campaign import CampaignCreate
from app.models.user import UserCreate
from app.db.database import db_create_campaign, db_init, db_create_user


def init_db():
    print("Initializing database")
    db_init()


# Create seeded user
def create_user():
    print("Creating seeded user")
    user = UserCreate(name="Diivix", email="diivix@chronicle.com", password="password")
    db_user = db_create_user(user)
    print(db_user)
    return db_user


# Create seeded user
def create_campaign(user: UserCreate):
    print("Creating seeded campaign")

    campaign = CampaignCreate(
        name="My Campaign",
        description="A simple campaign",
    )
    db_campaign = db_create_campaign(campaign, user)
    print(db_campaign)
    return db_campaign


if __name__ == "__main__":
    init_db()
    user = create_user()
    campaign = create_campaign(user)
