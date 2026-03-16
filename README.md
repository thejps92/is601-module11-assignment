# FastAPI Calculator Application

## Overview
This project is a web calculator built with FastAPI.
It provides:
- A browser UI with two number inputs and operation buttons
- REST API endpoints for add, subtract, multiply, and divide
- Input validation and structured error handling
- Logging for successful operations and errors
- Automated testing with unit, integration, and end-to-end tests
- Docker support and GitHub Actions CI/CD

## Features
- Server-rendered homepage at /
- API endpoints:
  - POST /add
  - POST /subtract
  - POST /multiply
  - POST /divide
- JSON request body format:

```json
{
  "a": 10,
  "b": 5
}
```

- JSON success response format:

```json
{
  "result": 15
}
```

- JSON error response format:

```json
{
  "error": "Cannot divide by zero!"
}
```

## Project Structure

```text
is601-module8-assignment/
├── app/
│   └── operations/
│       └── __init__.py
├── templates/
│   └── index.html
├── tests/
│   ├── conftest.py
│   ├── unit/
│   │   └── test_calculator.py
│   ├── integration/
│   │   └── test_fastapi_calculator.py
│   └── e2e/
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

### 3. Stop containers

```powershell
docker compose down
```

### 4. Open in browser
- http://localhost:8000

## CI/CD
- GitHub Actions runs the pipeline on push and pull request events for main.
- Stages: test, security scan, and deploy.
- On successful deploy from main, a new Docker image is pushed to Docker Hub.

Docker Hub repository:
- https://hub.docker.com/r/jps92/is601-module8-assignment
