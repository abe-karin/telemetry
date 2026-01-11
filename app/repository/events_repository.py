# app/repository/events_repository.py

import json
from app.database.connection import get_connection
from app.models import UserActionEvent


class EventsRepository:
    def __init__(self):
        self._create_table()

    def _create_table(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS events (
                event_id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                action TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                source TEXT NOT NULL,
                metadata TEXT
            )
            """
        )

        conn.commit()
        conn.close()

    def save(self, event: UserActionEvent):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO events (
                event_id, user_id, action, timestamp, source, metadata
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                str(event.event_id),
                event.user_id,
                event.action,
                event.timestamp.isoformat(),
                event.source,
                json.dumps(event.metadata),
            ),
        )

        conn.commit()
        conn.close()
