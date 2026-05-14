
# Smart API Rate Limiter & Usage Analytics Backend

A production-style backend project built using FastAPI, PostgreSQL and Docker.

I built this project to learn how real backend systems are structured and deployed. The project focuses on API authentication, request tracking, rate limiting, analytics, Dockerization and cloud deployment.

The backend allows users to generate API keys, access protected routes, track API usage and view request analytics.


# Features

* API Key Authentication
* Protected Routes
* PostgreSQL Database Integration
* Request Logging System
* Usage Analytics Endpoint
* PostgreSQL-Based Rate Limiting
* Dockerized Backend Setup
* Environment Variable Configuration
* Swagger API Documentation
* Health Check Endpoint
* Production-Style Logging Middleware
* Railway Deployment



# Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* Pydantic
* Docker
* Docker Compose
* Railway
* python-dotenv



# Project Structure

```bash id="n26p9o"
app/
│
├── main.py
├── config.py
├── models.py
├── schemas.py
│
├── db/
├── routes/
├── services/
├── utils/
├── docker/
│
├── docker-compose.yml
├── requirements.txt
├── .env
├── .dockerignore
```

---

# Main Functionalities

## User Creation

Users can be created and stored inside PostgreSQL.

---

## API Key Generation

Each user can generate secure API keys for authentication.

---

## Protected Routes

Routes are protected using API key authentication.

Example header:

```http id="7r6q0x"
x-api-key: YOUR_API_KEY
```

---

## Request Logging

Every API request is logged into PostgreSQL for analytics and tracking.

---

## Rate Limiting

The backend limits requests per user within a time window using PostgreSQL-based tracking.

---

## Analytics Endpoint

Users can view API usage analytics and request activity.

---

# API Endpoints

## User Routes

```http id="r8sld5"
POST /users/create
```

---

## API Key Routes

```http id="nd1h1e"
POST /apikeys/generate
```

---

## Protected Route

```http id="mt5mrh"
GET /protected
```

---

## Analytics Route

```http id="7i4s3h"
GET /analytics
```

---

## Utility Routes

```http id="d6gz72"
GET /health
```

```http id="8f22ji"
GET /
```

---

# Local Setup

## Clone Repository

```bash id="w06cc3"
git clone <your-repo-url>
```

---

## Create Virtual Environment

```bash id="m2nq7z"
python -m venv venv
```

Activate environment:

### Windows

```bash id="we8jlwm"
venv\Scripts\activate
```

---

## Install Requirements

```bash id="6oq7p5"
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env id="7klcjq"
DATABASE_URL=your_database_url

RATE_LIMIT_PER_MINUTE=10
```

---

## Run Backend

```bash id="1ibqbo"
uvicorn main:app --reload
```

---

# Docker Setup

Run:

```bash id="4w1em8"
docker compose up --build
```

Swagger Docs:

```bash id="g7jlwm"
http://localhost:8000/docs
```

---

# Live Deployment

Backend deployed on Railway:

```text id="3ljnho"
https://your-project.up.railway.app
```

Swagger Docs:

```text id="33t9m0"
https://your-project.up.railway.app/docs
```

---


# Author

Built by a Computer Science student learning backend engineering and production-style API development.
