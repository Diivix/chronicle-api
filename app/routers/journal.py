from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session

from ..models.journal_entry import JournalEntryCreate, JournalEntryRead
from ..models.campaign import CampaignCreate, CampaignRead
from ..db.database import (
    db_create_campaign,
    db_create_journal_entry,
    db_delete_campaign,
    db_get_all_user_campaigns,
    db_get_campaign,
    db_get_user,
    get_db_session,
)


router = APIRouter(
    prefix="/journal", tags=["journal"], responses={404: {"description": "Not found"}}
)

# Campaigns

# Create new campaign
@router.post(path="/campaign", response_model=CampaignRead)
def create_campaign(
    *, db_session: Session = Depends(get_db_session), campaign: CampaignCreate
) -> CampaignRead:
    # TODO: Fix user after auth is implemented
    user = db_get_user(db_session, 1)
    return db_create_campaign(db_session, campaign, user)


# Get a single campaign
@router.get(path="/campaign/{id}", response_model=CampaignRead)
def campaign(*, db_session: Session = Depends(get_db_session), id: int) -> CampaignRead:
    # TODO: Fix user after auth is implemented
    user = db_get_user(db_session, 1)
    return db_get_campaign(db_session, id, user)


# Get all campaigns
@router.get(path="/campaigns", response_model=List[CampaignRead])
def campaigns(*, db_session: Session = Depends(get_db_session)) -> List[CampaignRead]:
    # TODO: Fix user after auth is implemented
    user = db_get_user(db_session, 1)
    return db_get_all_user_campaigns(db_session, user)


# Delete a campaign
@router.delete(path="/campaign/{id}", response_model=str)
def delete_campaign(*, db_session: Session = Depends(get_db_session), id: int) -> str:
    # TODO: Fix user after auth is implemented
    user = db_get_user(db_session, 1)
    result = db_delete_campaign(db_session, id, user)
    if result:
        return "Campaign deleted"
    else:
        return "Campaign not found or not deleted"


# Journal entries

# Create new journal entry
@router.post(path="/{campaign_id}/entry", response_model=JournalEntryRead)
def create_entry(
    *,
    db_session: Session = Depends(get_db_session),
    campaign_id: int,
    entry: JournalEntryCreate
) -> JournalEntryRead:
    # TODO: Fix user after auth is implemented
    user = db_get_user(db_session, 1)
    return db_create_journal_entry(db_session, entry, campaign_id, user)


# # Get a single journal entry in a campaign
# @router.get("/{campaign}/entry/{id}")
# def entry(*, db_session: Session = Depends(get_db_session), campaign: str, id: int):
#     return {"value": id}


# # Get all journal entries to a campaign
# @router.get("/campaign/{campaign}")
# def campaign(*, db_session: Session = Depends(get_db_session), campaign: str):
#     return {"campaign": campaign}


# # Update a campaign
# @router.put("/{campaign}")
# def update_campaign(*, db_session: Session = Depends(get_db_session), campaign: str, campaign_request: CampaignRequest):
#     return {"campaign": campaign}


# # Update a single journal entry in a campaign
# @router.put("/{campaign}/entry/{id}")
# def update_entry(*, db_session: Session = Depends(get_db_session), campaign: str, id: int, entry: JournalEntryRequest):
#     return {"value": id}


# # Delete a single journal entry in a campaign
# @router.delete(path="/journal/{campaign}/entry/{id}", response_model=bool)
# def delete_entry(*, db_session: Session = Depends(get_db_session), campaign: str, id: int):
#     return {"value": id}
