## Makefile for common development tasks

.PHONY: help dev build run compose-up compose-down lint

help:
	@echo "Available targets:"
	@echo "  make dev         # start uvicorn in development mode"
	@echo "  make build       # build docker image"
	@echo "  make run         # run docker image locally"
	@echo "  make compose-up  # docker compose up"
	@echo "  make compose-down# docker compose down"
	@echo "  make lint        # run basic lint (if configured)"

dev:
	python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

build:
	docker build -t fastapi-kong:local .

run: build
	docker run --rm -p 8000:8000 fastapi-kong:local

compose-up:
	docker compose up --build

compose-down:
	docker compose down --volumes --remove-orphans

lint:
	@echo "No linter configured. Add a linter command here (flake8/ruff/markdownlint)."
kong-postgres:
	COMPOSE_PROFILES=database KONG_DATABASE=postgres docker compose up -d

kong-dbless:
	docker compose up -d

clean:
	docker compose kill
	docker compose rm -f