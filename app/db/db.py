from ast import List
from sqlmodel import Field, Session, SQLModel, create_engine, select

from ..models.campaign import Campaign, CampaignBase, CampaignCreate, CampaignRead

sqlite_file_name = "data/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def db_init():
    """Create db and tables if they don't exist."""
    SQLModel.metadata.create_all(engine)

def db_create_campaign(campaign: Campaign) -> CampaignRead:
    with Session(engine) as session:
        db_campaign = Campaign.from_orm(campaign)
        session.add(db_campaign)
        session.commit()
        session.refresh(db_campaign)
        return db_campaign

def db_get_campaign(name: str) -> CampaignRead:
    with Session(engine) as session:
        statement = select(Campaign).where(Campaign.name == name)
        results = session.execute(statement)
        return results

def db_get_all_campaigns() -> List[CampaignRead]:
    with Session(engine) as session:
        statement = select(Campaign)
        results = session.execute(statement).all()
        return results
