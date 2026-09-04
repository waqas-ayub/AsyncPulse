import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('asyncpulse')

# Django settings se CELERY namespace wale config read karega
app.config_from_object('django.conf:settings', namespace='CELERY')

# Sub installed apps me se tasks.py automatically discover karega
app.autodiscover_tasks()