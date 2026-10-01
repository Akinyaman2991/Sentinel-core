# 🛡️ SentinelCore

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**SentinelCore** is an enterprise-grade, high-performance **distributed event streaming and audit log processing engine** designed for modern microservices architectures and high-throughput environments.

The platform asynchronously ingests log/event streams, persists them in a relational database, and routes critical events (such as `CRITICAL` severity errors) to a **Celery & Redis** task queue for real-time background execution, anomaly detection, and alert webhook triggers.

---

## 📋 Table of Contents

- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Directory Structure](#-directory-structure)
- [Quick Start](#-quick-start)
- [Environment Variables (.env)](#-environment-variables-env)
- [API Documentation & Usage](#-api-documentation--usage)
- [Running Tests](#-running-tests)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Key Features

* **⚡ High Throughput:** Built on FastAPI and ASGI for non-blocking asynchronous request handling.
* **🔄 Distributed Background Tasks:** Heavy background processes are offloaded from the primary API server to Celery workers using Redis Pub/Sub.
* **🗄️ Asynchronous ORM Layer:** Fully asynchronous database transactions powered by `SQLAlchemy 2.0` and `asyncpg` over PostgreSQL.
* **🛡️ Data Validation:** Strict type safety and runtime schema validation enforced by `Pydantic v2`.
* **🐳 Fully Dockerized Environment:** Single-command setup to orchestrate API nodes, Workers, PostgreSQL, and Redis instances via `docker-compose`.
* **🧪 Comprehensive Testing:** Pre-configured integration test suite using `pytest` and `httpx`.

---

## 🏗️ System Architecture

```text
               +-----------------------+
               |  Microservices / API  |
               +-----------+-----------+
                           |
                           | (HTTP POST /api/v1/events)
                           v
               +-----------------------+
               |   SentinelCore API    |
               |       (FastAPI)       |
               +----+-------------+----+
                    |             |
     (Async Save)   |             | (Enqueue Task)
                    v             v
          +-----------+         +-----------+
          | PostgreSQL|         |   Redis   |
          +-----------+         +-----+-----+
                                      |
                                      v
                                +-----------+
                                |  Celery   |
                                |  Workers  |
                                +-----------+
