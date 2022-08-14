from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from ..models.journal_entry import JournalEntry, JournalEntryCreate, JournalEntryRead
from ..models.campaign import CampaignCreate, CampaignRead
from ..db.database import (
    db_create_campaign,
    db_create_journal_entry,
    db_delete_campaign,
    db_delete_journal_entry,
    db_get_all_user_campaigns,
    db_get_campaign,
    db_get_campaign_journal_entries,
    db_get_journal_entry,
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
@router.get(path="/campaign/{campaign_id}", response_model=CampaignRead)
def campaign(
    *, db_session: Session = Depends(get_db_session), campaign_id: int
) -> CampaignRead:
    # TODO: Fix user after auth is implemented
    user = db_get_user(db_session, 1)
    result = db_get_campaign(db_session, campaign_id, user)
    if result is None:
        raise HTTPException(status_code=404, detail="Campaign not found.")
    return result


# Get all campaigns
@router.get(path="/campaigns", response_model=List[CampaignRead])
def campaigns(*, db_session: Session = Depends(get_db_session)) -> List[CampaignRead]:
    # TODO: Fix user after auth is implemented
    user = db_get_user(db_session, 1)
    return db_get_all_user_campaigns(db_session, user)


# TODO: Add an update route for journal entries

# Delete a campaign
@router.delete(path="/campaign/{campaign_id}", response_model=str)
def delete_campaign(
    *, db_session: Session = Depends(get_db_session), campaign_id: int
) -> str:
    # TODO: Fix user after auth is implemented
    user = db_get_user(db_session, 1)
    result = db_delete_campaign(db_session, campaign_id, user)
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


# Get a single journal entry in a campaign
@router.get(path="/entry/{campaign_id}/{entry_id}", response_model=JournalEntryRead)
def journal_entry(
    *, db_session: Session = Depends(get_db_session), campaign_id: int, entry_id: int
):
    # TODO: Fix user after auth is implemented
    user = db_get_user(db_session, 1)
    result = db_get_journal_entry(db_session, campaign_id, entry_id, user)
    if result is None:
        raise HTTPException(
            status_code=404, detail="Journal entry not found or not accessible."
        )
    return result


# Get all journal entries for a campaign
@router.get("/entries/campaign/{campaign_id}", response_model=List[JournalEntryRead])
def campaign_journal_entries(
    *, db_session: Session = Depends(get_db_session), campaign_id: int
):
    # TODO: Fix user after auth is implemented
    user = db_get_user(db_session, 1)
    results = db_get_campaign_journal_entries(db_session, campaign_id, user)
    return results


# TODO: Add an update route for journal entries

# Delete a single journal entry
@router.delete(path="/entry/{campaign_id}/{entry_id}", response_model=str)
def delete_journal_entry(
    *, db_session: Session = Depends(get_db_session), campaign_id: int, entry_id: int
) -> str:
    # TODO: Fix user after auth is implemented
    user = db_get_user(db_session, 1)
    result = db_delete_journal_entry(db_session, campaign_id, entry_id, user)
    if result:
        return "Journal entry deleted"
    else:
        return "Journal entry not found or not accessible"
