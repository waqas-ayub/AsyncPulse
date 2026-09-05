import logging
import requests
from celery import shared_task
from django_celery_results.models import TaskResult
from django.utils import timezone
from datetime import timedelta

logger = logging.getLogger(__name__)

@shared_task(
    bind=True,
    max_retries=3,
    default_retry_delay=5,
    autoretry_for=(requests.RequestException, Exception),
    retry_backoff=True,
    rate_limit='10/m',  # Maximum 10 tasks per minute
)
def send_webhook_notification(self, target_url, payload):
    """
    Background task to send Webhooks with Auto-Retry and Rate Limiting (10/min).
    """
    logger.info(f"Triggering webhook to {target_url} [Attempt {self.request.retries + 1}]")
    
    try:
        response = requests.post(target_url, json=payload, timeout=10)
        response.raise_for_status()
        logger.info(f"Webhook delivered successfully to {target_url}")
        return {
            "status": "SUCCESS", 
            "status_code": response.status_code,
            "target_url": target_url
        }
        
    except requests.RequestException as exc:
        logger.error(f"Webhook delivery failed to {target_url}: {str(exc)}")
        raise self.retry(exc=exc)


@shared_task
def cleanup_old_task_results(days=7):
    """
    Periodic background task to remove task result logs older than `days`.
    """
    cutoff_date = timezone.now() - timedelta(days=days)
    deleted_count, _ = TaskResult.objects.filter(date_done__lt=cutoff_date).delete()
    logger.info(f"Automated Cleanup: Purged {deleted_count} expired task results older than {days} days.")
    return {"purged_records": deleted_count}