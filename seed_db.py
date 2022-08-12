import hashlib
from datetime import datetime
from ssl import create_default_context
from time import sleep
from app.models.campaign import Campaign, CampaignCreate
from app.models.user import User, UserCreate
from app.db.db import db_create_campaign, db_get_user, db_init, db_create_user


def init_db():
    print("Initializing database")
    db_init()


# Create seeded user
def create_user():
    print("Creating seeded user")
    user = UserCreate(
        name="Diivix",
        email="diivix@chronicle.com",
        password="password"
    )
    created_user = db_create_user(user)
    print(created_user)


# Create seeded user
def create_campaign():
    print("Creating seeded campaign")
    user = db_get_user(1)
    print(user)

    campaign = CampaignCreate(
        name="My Campaign",
        description="A simple campaign",
    )
    create_campaign = db_create_campaign(campaign, user)
    print(create_campaign)


if __name__ == "__main__":
    init_db()
    create_user()
    create_campaign()
