from datetime import datetime
from fastapi import APIRouter

from ..db.db import db_create_campaign, db_deactivate_campaign, db_get_all_campaigns, db_get_campaign, db_get_user

from ..models.campaign import Campaign, CampaignCreate

router = APIRouter()

# Campaigns

# Create new campaign
@router.post("/journal/campaign")
def create_campaign(campaign: CampaignCreate):
    # TODO: change this
    user = db_get_user(1)
    return db_create_campaign(campaign, user)

# Get a single campaign
@router.get("/journal/campaign/{id}")
def campaign(id: int):
    return db_get_campaign(id)


# Get all campaigns
@router.get("/journal/campaigns")
def campaigns():
    return db_get_all_campaigns()


# Delete a campaign
@router.delete("/journal/campaign/{id}")
def delete_campaign(id: int):
    return db_deactivate_campaign(id)


# Journal entries

# # Create new journal entry
# @router.post("/journal/{campaign}/entry")
# def create_entry(campaign: str, entry: JournalEntryRequest):
#     return "healthy"


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


# Delete a single journal entry in a campaign
@router.delete("/journal/{campaign}/entry/{id}")
def delete_entry(campaign: str, id: int):
    return {"value": id}
