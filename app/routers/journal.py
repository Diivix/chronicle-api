from datetime import datetime
from fastapi import APIRouter

from ..db.db import db_create_campaign

from ..models.campaign import Campaign, CampaignCreate

router = APIRouter()

# Create new campaign
@router.post("/journal")
def create_campaign(campaign: CampaignCreate):
    updated_campaign = Campaign(**campaign.dict())
    now = datetime.now().isoformat()
    updated_campaign.created = now
    updated_campaign.updated = now
    db_create_campaign(updated_campaign)
    return campaign


# # Create new journal entry
# @router.post("/journal/{campaign}/entry")
# def create_entry(campaign: str, entry: JournalEntryRequest):
#     return "healthy"


# Get all journal entries to a campaign
@router.get("/journal/{campaign}")
def campaign(campaign: str):
    return {"campaign": campaign}


# # Get a single journal entry in a campaign
# @router.get("/journal/{campaign}/entry/{id}")
# def entry(campaign: str, id: int):
#     return {"value": id}


# # Update a campaign
# @router.put("/journal/{campaign}")
# def update_campaign(campaign: str, campaign_request: CampaignRequest):
#     return {"campaign": campaign}


# # Update a single journal entry in a campaign
# @router.put("/journal/{campaign}/entry/{id}")
# def update_entry(campaign: str, id: int, entry: JournalEntryRequest):
#     return {"value": id}


# Delete a campaign
@router.delete("/journal/{campaign}")
def delete_campaign(campaign: str):
    return {"campaign": campaign}


# Delete a single journal entry in a campaign
@router.delete("/journal/{campaign}/entry/{id}")
def delete_entry(campaign: str, id: int):
    return {"value": id}
