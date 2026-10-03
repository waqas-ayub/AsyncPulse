# ⚡ AsyncPulse: Production-Grade Asynchronous Task & Webhook Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-092E20.svg)](https://www.djangoproject.com/)
[![Celery](https://img.shields.io/badge/Celery-5.x-37814A.svg)](https://docs.celeryq.dev/)
[![Redis](https://img.shields.io/badge/Redis-Latest-DC382D.svg)](https://redis.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**AsyncPulse** is a scalable, reliable, fault-tolerant, and observable background task execution engine built using **Django 5, Celery 5, Redis, and Django REST Framework**. It is designed to handle high-concurrency background job processing, automated webhook dispatching with retries, and real-time task status tracking without blocking the main application interface.

---

## 🖥️ Live Operational Dashboard Showcase

### 1. Webhook Dispatcher & Health Monitor Interface
Interactive control center displaying real-time system health checks (Database & Redis connection status) alongside the webhook task dispatcher:

![AsyncPulse Dashboard Idle State](<img width="959" height="479" alt="Screenshot 2026-10-03 111349" src="https://github.com/user-attachments/assets/26da8f29-f6c3-4f1f-9e21-54937241da1c" />
)

### 2. Live Task Stream & Asynchronous Worker Execution
Real-time polling stream showcasing active task execution (`STATUS: 200 SUCCESS`), unique task tracking UUIDs, and live JSON payload responses processed by Celery workers:

![AsyncPulse Task Execution Stream](<img width="958" height="479" alt="Screenshot 2026-10-03 111501" src="https://github.com/user-attachments/assets/361749a2-a01b-46c5-b4d3-16d88b28f8bf" />)

> **Note:** To ensure images display properly, create an `assets` folder in your repository root and upload your screenshots named `dashboard-idle.png` and `task-success.png`.

---

## 🚀 Key Features

* **Asynchronous Webhook Engine:** Automated external webhooks delivery pipeline powered by Celery with exponential backoff retries.
* **Task Throttling & Rate Limiting:** Strictly enforces per-task execution limits (e.g., 10 tasks/minute) to prevent server exhaustion and downstream API rate limits.
* **Task Status Tracking:** Live background task status polling (`PENDING`, `STARTED`, `SUCCESS`, `FAILURE`) using `AsyncResult` integration.
* **System Observability & Diagnostics:** Health check API (`/api/health/`) inspecting DB & Redis connection health in real-time.
* **Automated Cleanups:** Scheduled daily purging of old task execution records via **Celery Beat** to keep the database lightweight and optimized.

---

## 🛠 Tech Stack & Architecture

* **Backend Framework:** Django 5.x & Django REST Framework (DRF)
* **Task Queue:** Celery 5.x
* **Message Broker:** Redis
* **Result Backend:** `django-celery-results` (Database Backend)
* **Authentication:** JWT (SimpleJWT)
* **Frontend UI:** React.js / Vite Operational Dashboard (Deployed on Vercel)

---

## ⚙️ Local Setup Instructions

### 1. Repository Clone & Environment Setup
```bash
git clone [https://github.com/waqas-ayub/AsyncPulse.git](https://github.com/waqas-ayub/AsyncPulse.git)
cd AsyncPulse

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1   # Windows PowerShell
# source venv/bin/activate    # Linux/macOS
