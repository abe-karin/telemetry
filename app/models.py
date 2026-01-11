# app/models.py

from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import UUID, uuid4
from typing import Dict, Any


class UserActionEvent(BaseModel):
    event_id: UUID = Field(default_factory=uuid4)
    user_id: str
    action: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    source: str = "api"
    metadata: Dict[str, Any] = Field(default_factory=dict)
