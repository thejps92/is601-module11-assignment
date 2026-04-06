# FastAPI Calculator Application

## Overview
This project is a web calculator built with FastAPI.

It includes:
- A browser UI with two number inputs and operation buttons
- REST API endpoints for add, subtract, multiply, and divide
- Input validation and structured error handling
- Logging for successful operations and errors
- A minimal secure user model (SQLAlchemy + Pydantic) for Module 10
- Password hashing + verification (bcrypt via Passlib)
- Automated testing with unit, integration, and end-to-end tests
- Docker support and GitHub Actions CI/CD

## Project Structure

```text
is601-module10-assignment/
├── app/
│   ├── auth/
│   │   ├── __init__.py
│   │   └── security.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── operations/
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   └── database_init.py
├── templates/
│   └── index.html
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   │   ├── test_calculator.py
│   │   ├── test_database.py
│   │   ├── test_database_init.py
│   │   ├── test_security.py
│   │   ├── test_user_model.py
│   │   └── test_user_schema.py
│   ├── integration/
│   │   ├── conftest.py
│   │   ├── test_fastapi_calculator.py
│   │   └── test_user_database.py
│   └── e2e/
│       ├── conftest.py
│       └── test_e2e.py
├── .github/workflows/
│   └── ci.yml
├── main.py
├── requirements.txt
├── Dockerfile
├── compose.yaml
└── README.md
```

## Prerequisites
- Python 3.10 to 3.12 recommended
- Docker Desktop

## Run Locally (PowerShell)

### 1. Set up environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install
```

### 2. Start application

```powershell
uvicorn main:app --reload
```

### 3. Open in browser
- http://127.0.0.1:8000

## Run with Docker

### 1. Build and start

```powershell
docker compose up --build
```

### 2. Run in background (optional)

```powershell
docker compose up --build -d
```

### 3. Open in browser
- http://127.0.0.1:8000

### 4. Stop containers

```powershell
docker compose down
```

## Run Tests Locally (Brief)
All commands below assume your virtual environment is activated.

### Unit tests
```powershell
python -m pytest tests\unit -q
```

### Integration tests (requires a real Postgres database)
Integration tests require `DATABASE_URL`.

Example:
```powershell
$env:DATABASE_URL = "postgresql://user:password@localhost:5432/myappdb"
python -m pytest tests\integration -q
```

### End-to-end (E2E) tests
```powershell
python -m pytest tests\e2e -q
```

## CI/CD
- GitHub Actions runs the pipeline on push and pull request events for main.
- Stages: test, security scan, and deploy.
- On successful deploy from main, a new Docker image is pushed to Docker Hub.

Docker Hub repository:
- https://hub.docker.com/r/jps92/is601-module10-assignment