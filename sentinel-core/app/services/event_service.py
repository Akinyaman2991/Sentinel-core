from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.event import EventModel
from app.schemas.event import EventCreate

class EventService:
    @staticmethod
    async def create_event(db: AsyncSession, event_in: EventCreate) -> EventModel:
        db_event = EventModel(
            service_name=event_in.service_name,
            event_type=event_in.event_type,
            severity=event_in.severity,
            payload=event_in.payload,
            user_id=event_in.user_id
        )
        db.add(db_event)
        await db.commit()
        await db.refresh(db_event)
        return db_event

    @staticmethod
    async def get_events(db: AsyncSession, limit: int = 50, severity: str = None):
        query = select(EventModel).order_by(EventModel.created_at.desc()).limit(limit)
        if severity:
            query = query.where(EventModel.severity == severity)
        result = await db.execute(query)
        return result.scalars().all()