# 🛡️ SentinelCore - Distributed Event & Log Processing Platform

High-performance, asynchronous log ingestion and processing engine built with Python, FastAPI, PostgreSQL, Redis, and Celery.

## 🏗️ Architecture Overview
- **FastAPI**: Non-blocking asynchronous REST API layer.
- **PostgreSQL**: Relational storage for audit logs using `asyncpg` and SQLAlchemy 2.0.
- **Redis & Celery**: Distributed task queue for asynchronous processing and alerts.
- **Docker & Docker Compose**: Unified setup for easy development and deployment.

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/sentinel-core.git](https://github.com/Akinyaman2991/sentinel-core.git)
cd sentinel-core