# ⚡ AsyncPulse — Production-Grade Asynchronous Task & Webhook Engine

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-092E20.svg)](https://www.djangoproject.com/)
[![Celery](https://img.shields.io/badge/Celery-5.x-37814A.svg)](https://docs.celeryq.dev/)
[![Redis](https://img.shields.io/badge/Redis-Latest-DC382D.svg)](https://redis.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**AsyncPulse** is a scalable, reliable, fault-tolerant, and observable background task execution engine built using **Django 5, Celery 5, Redis, and Django REST Framework**[cite: 1, 7]. It is designed to handle high-concurrency background job processing, automated webhook dispatching with retries, and real-time task status tracking without blocking the main application interface[cite: 1].

---

## 🖥️ Live Operational Dashboard Showcase

### 1. Webhook Dispatcher & Health Monitor Interface
Interactive control center displaying real-time system health checks (Database & Redis connection status) alongside the webhook task dispatcher:

![AsyncPulse Dashboard Idle State](https://raw.githubusercontent.com/waqas-ayub/AsyncPulse/main/assets/dashboard-idle.png)[cite: 5]

### 2. Live Task Stream & Asynchronous Worker Execution
Real-time polling stream showcasing active task execution (`STATUS: 200 SUCCESS`), unique task tracking UUIDs, and live JSON payload responses processed by Celery workers:

![AsyncPulse Task Execution Stream](https://raw.githubusercontent.com/waqas-ayub/AsyncPulse/main/assets/task-success.png)[cite: 6]

> **Note:** To render images above, ensure you upload the screenshots into an `assets/` directory in your GitHub repository root as `dashboard-idle.png`[cite: 5] and `task-success.png`[cite: 6].

---

## 🚀 Key Features

* **Asynchronous Webhook Engine:** Automated external webhooks delivery pipeline powered by Celery with exponential backoff retries[cite: 1, 7].
* **Task Throttling & Rate Limiting:** Strictly enforces per-task execution limits (e.g., 10 tasks/minute) to prevent server exhaustion and downstream API rate limits[cite: 1, 7].
* **Task Status Tracking:** Live background task status polling (`PENDING`, `STARTED`, `SUCCESS`, `FAILURE`) using `AsyncResult` integration[cite: 1, 7].
* **System Observability & Diagnostics:** Health check API (`/api/health/`) inspecting DB & Redis connection health in real-time.
* **Automated Cleanups:** Scheduled daily purging of old task execution records via **Celery Beat** to keep the database lightweight and optimized[cite: 1, 7].

---

## 🛠 Tech Stack & Architecture

* **Backend Framework:** Django 5.x & Django REST Framework (DRF)[cite: 1, 7]
* **Task Queue:** Celery 5.x[cite: 1, 7]
* **Message Broker:** Redis[cite: 1, 7]
* **Result Backend:** `django-celery-results` (Database Backend)[cite: 1, 7]
* **Authentication:** JWT (SimpleJWT)[cite: 1]
* **Frontend UI:** React.js / Vite Operational Dashboard (Deployed on Vercel)[cite: 5, 6]

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
