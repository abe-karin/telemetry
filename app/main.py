# app/main.py

from fastapi import FastAPI, Request, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
import time
import logging

from app.models import UserActionEvent
from app.logging_config import setup_logging
from app.services.event_service import EventService
from app.observability.metrics import (
    http_requests_total,
    http_request_duration_seconds,
)

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="Telemetry Mini Service")
event_service = EventService()


@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response: Response = await call_next(request)
    duration = time.time() - start_time

    endpoint = request.url.path

    http_requests_total.labels(
        method=request.method,
        endpoint=endpoint,
        status=response.status_code
    ).inc()

    http_request_duration_seconds.labels(
        endpoint=endpoint
    ).observe(duration)

    return response


@app.post("/actions")
def create_action(event: UserActionEvent):
    event_service.register_event(event)
    return {"status": "stored", "event_id": event.event_id}


@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )
