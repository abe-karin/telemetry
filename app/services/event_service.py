# app/services/event_service.py

from app.models import UserActionEvent
from app.repository.events_repository import EventsRepository
from app.observability.metrics import user_actions_total
import logging

logger = logging.getLogger(__name__)


class EventService:
    def __init__(self):
        self.repository = EventsRepository()

    def register_event(self, event: UserActionEvent):
        logger.info(
            "persisting_user_action_event",
            extra={
                "extra": {
                    "event_id": str(event.event_id),
                    "action": event.action,
                }
            },
        )

        # Métrica de domínio
        user_actions_total.labels(
            action=event.action,
            source=event.source
        ).inc()

        self.repository.save(event)
