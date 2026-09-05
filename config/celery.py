import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('asyncpulse')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Celery Beat Periodic Tasks Configuration
app.conf.beat_schedule = {
    'cleanup-expired-task-results-daily': {
        'task': 'core.tasks.cleanup_old_task_results',
        'schedule': crontab(hour=0, minute=0),  # Runs daily at midnight
    },
}