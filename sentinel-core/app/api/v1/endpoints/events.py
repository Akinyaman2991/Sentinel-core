from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from app.db.session import get_db
from app.schemas.event import EventCreate, EventResponse
from app.services.event_service import EventService
from app.core.celery_app import process_heavy_log_event

router = APIRouter()

@router.post("/", response_model=EventResponse, status_code=status.HTTP_202_ACCEPTED)
async def ingest_event(
    event_in: EventCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Log/Event verisini asenkron olarak veritabanına kaydeder ve
    Celery worker kuyruğuna aktarır.
    """
    # 1. Veritabanına kaydet
    db_event = await EventService.create_event(db, event_in)
    
    # 2. Celery kuyruğuna gönder (Kuyruğu kilitlemeden devam eder)
    event_payload = {
        "id": str(db_event.id),
        "service_name": db_event.service_name,
        "severity": db_event.severity,
        "event_type": db_event.event_type,
        "payload": db_event.payload
    }
    process_heavy_log_event.delay(event_payload)

    return db_event

@router.get("/", response_model=List[EventResponse])
async def list_events(
    limit: int = Query(50, ge=1, le=100),
    severity: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """
    Son kaydedilen event'leri listeler (Severity filtresi destekler).
    """
    return await EventService.get_events(db, limit=limit, severity=severity)