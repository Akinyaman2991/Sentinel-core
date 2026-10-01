from fastapi import APIRouter
from app.api.v1.endpoints import events

api_router = APIRouter()
api_router.include_router(events.router, prefix="/events", tags=["Events"])