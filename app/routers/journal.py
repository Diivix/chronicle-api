from typing import List
from fastapi import APIRouter

from ..models.journal_entry import JournalEntryCreate, JournalEntryRead

from ..db.database import (
    db_create_campaign,
    db_create_journal_entry,
    db_delete_campaign,
    db_get_all_user_campaigns,
    db_get_campaign,
    db_get_user,
)

from ..models.campaign import CampaignCreate, CampaignRead

router = APIRouter()

# Campaigns

# Create new campaign
@router.post(path="/journal/campaign", response_model=CampaignRead)
def create_campaign(campaign: CampaignCreate) -> CampaignRead:
    # TODO: Fix user after auth is implemented
    user = db_get_user(1)
    return db_create_campaign(campaign, user)


# Get a single campaign
@router.get(path="/journal/campaign/{id}", response_model=CampaignRead)
def campaign(id: int) -> CampaignRead:
    # TODO: Fix user after auth is implemented
    user = db_get_user(1)
    return db_get_campaign(id, user)


# Get all campaigns
@router.get(path="/journal/campaigns", response_model=List[CampaignRead])
def campaigns() -> List[CampaignRead]:
    # TODO: Fix user after auth is implemented
    user = db_get_user(1)
    return db_get_all_user_campaigns(user)


# Delete a campaign
@router.delete(path="/journal/campaign/{id}", response_model=str)
def delete_campaign(id: int) -> str:
    # TODO: Fix user after auth is implemented
    user = db_get_user(1)
    result = db_delete_campaign(id, user)
    if result:
        return "Campaign deleted"
    else:
        return "Campaign not found or not deleted"


# Journal entries

# Create new journal entry
@router.post(path="/journal/{campaign_id}/entry", response_model=JournalEntryRead)
def create_entry(campaign_id: int, entry: JournalEntryCreate) -> JournalEntryRead:
    # TODO: Fix user after auth is implemented
    user = db_get_user(1)
    return db_create_journal_entry(entry, campaign_id, user)


# # Get a single journal entry in a campaign
# @router.get("/journal/{campaign}/entry/{id}")
# def entry(campaign: str, id: int):
#     return {"value": id}


# # Get all journal entries to a campaign
# @router.get("/journal/campaign/{campaign}")
# def campaign(campaign: str):
#     return {"campaign": campaign}


# # Update a campaign
# @router.put("/journal/{campaign}")
# def update_campaign(campaign: str, campaign_request: CampaignRequest):
#     return {"campaign": campaign}


# # Update a single journal entry in a campaign
# @router.put("/journal/{campaign}/entry/{id}")
# def update_entry(campaign: str, id: int, entry: JournalEntryRequest):
#     return {"value": id}


# # Delete a single journal entry in a campaign
# @router.delete(path="/journal/{campaign}/entry/{id}", response_model=bool)
# def delete_entry(campaign: str, id: int):
#     return {"value": id}
