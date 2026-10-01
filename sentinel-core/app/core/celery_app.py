from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "sentinel_tasks",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

@celery_app.task(name="process_heavy_log_event")
def process_heavy_log_event(event_data: dict):
    """
    Arka planda asenkron çalışacak Celery görevi.
    Burada anomali tespiti, webhook tetikleme veya mail bildirimi yapılır.
    """
    severity = event_data.get("severity")
    service = event_data.get("service_name")
    
    print(f"[CELERY WORKER] [{severity}] Service '{service}' event processed. Payload ID: {event_data.get('id')}")
    
    if severity == "CRITICAL":
        print(f"[ALERT TRIPPED] Triggering emergency webhook for service: {service}")
        
    return {"status": "processed", "event_id": event_data.get("id")}