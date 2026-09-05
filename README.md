# AsyncPulse - Production-Grade Asynchronous Execution Engine

AsyncPulse is a scalable, reliable, and observable background task execution system built using **Django**, **Celery**, **Redis**, and **Django REST Framework**.

## 🚀 Key Features
- **Asynchronous Webhook Engine:** Automated webhooks delivery with exponential backoff retries.
- **Task Throttling & Rate Limiting:** Per-task execution rate limit enforced (e.g., 10 tasks/minute).
- **Task Status Tracking:** Live status polling (`PENDING`, `SUCCESS`, `FAILURE`) using `AsyncResult`.
- **System Observability:** Health check API (`/api/health/`) inspecting DB & Redis status.
- **Automated Cleanups:** Scheduled daily purging of old task execution records via Celery Beat.

---

## 🛠 Tech Stack
- **Framework:** Django 5.x, Django REST Framework
- **Task Queue:** Celery 5.x
- **Message Broker:** Redis
- **Result Backend:** `django-celery-results` (Database Backend)
- **Authentication:** JWT (SimpleJWT)

---

## ⚙️ Local Setup Instructions

### 1. Repository Clone & Environment Setup
```bash
git clone [https://github.com/waqas-ayub/AsyncPulse.git](https://github.com/waqas-ayub/AsyncPulse.git)
cd AsyncPulse
python -m venv venv
.\venv\Scripts\Activate.ps1   # On Windows