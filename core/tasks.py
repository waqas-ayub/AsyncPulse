from celery import shared_task
import time

@shared_task
def send_welcome_email_task(user_email):
    time.sleep(3)  # Email service simulation
    return f"Email sent to {user_email}"

@shared_task
def generate_user_report_task(user_id):
    time.sleep(10)  # Heavy data processing simulation
    return f"Report generated for User ID: {user_id}"