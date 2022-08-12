import hashlib
from datetime import datetime
from ssl import create_default_context
from app.models.campaign import Campaign
from app.models.user import User
from app.db.db import db_create_campaign, db_get_user, db_init, db_create_user


def init_db():
    print("Initializing database")
    db_init()


# Create seeded user
def create_user():
    print("Creating seeded user")
    now = datetime.now().isoformat()
    password_hash = hashlib.md5(b"password").hexdigest()
    user = User(
        name="Diivix",
        email="diivix@chronicle.com",
        password_hash=password_hash,
        created=now,
        updated=now,
    )
    created_user = db_create_user(user)
    print(created_user)

# Create seeded user
def create_campaign():
    print("Creating seeded campaign")
    now = datetime.now().isoformat()

    user = db_get_user(1)
    print(user)

    campaign = Campaign(
        name="My Campaign",
        description="A simple campaign",
        created=now,
        updated=now
    )
    create_campaign = db_create_campaign(campaign, user)
    print(create_campaign)


if __name__ == "__main__":
    init_db()
    create_user()
    create_campaign()
