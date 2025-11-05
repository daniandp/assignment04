# Python Flask App with Docker and GitHub Actions - Assignment 04

Simple Flask app that reads environment variables and exposes two endpoints:

- `/` → returns `APP_MESSAGE`
- `/health` → returns `APP_HEALTH`

## How to run locally (with docker-compose)

1. Create `.env` with:
APP_MESSAGE="Hello from Python Flask in Docker!"
APP_HEALTH="Everything Good"
PORT=8085

2. Build and run:
docker compose up --build

3. Test:
http://localhost:8085/
http://localhost:8085/health

## GitHub Actions

Workflow (`.github/workflows/deploy.yml`) will:
- Create `.env` from repository secrets
- Build Docker image
- Run container and test endpoints

## Dependabot

Dependabot configured to run weekly for pip, Docker and GitHub Actions.