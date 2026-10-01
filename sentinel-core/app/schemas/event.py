from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any
from uuid import UUID

class EventBase(BaseModel):
    service_name: str = Field(..., example="auth-service")
    event_type: str = Field(..., example="LOGIN_FAILED")
    severity: str = Field(..., example="WARNING")
    payload: Dict[str, Any] = Field(default_factory=dict, example={"ip": "192.168.1.1", "attempts": 3})
    user_id: Optional[str] = Field(None, example="user_9921")

class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True