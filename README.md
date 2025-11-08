# fastapi-kong

A minimal FastAPI example integrated with Kong (API Gateway) and optional Postgres. Designed for local development, Docker, and quick experimentation with Kong routes and services.

# fastapi-kong

A minimal FastAPI example integrated with Kong (API Gateway) and optional Postgres. Designed for local development, Docker, and quick experimentation with Kong routes and services.

---

## Table of Contents

1. [Quick links](#quick-links)
1. [Requirements](#requirements)
1. [Quickstart — Local development](#quickstart--local-development)
1. [Docker](#docker)
1. [Docker Compose (app + Kong + Postgres)](#docker-compose-app--kong--postgres)
1. [Kong — Registering services and routes](#kong---registering-services-and-routes)
1. [Configuration & secrets](#configuration--secrets)
1. [Makefile](#makefile)
1. [Testing](#testing)
1. [Troubleshooting](#troubleshooting)
1. [Contributing](#contributing)
1. [License](#license)

---

## Quick links

- Source: `app/`
- Dockerfile: `Dockerfile`
- Compose: `docker-compose.yml`
- Kong declarative example: `config/kong.yaml`

## Requirements

1. Python 3.9+ (for local development)
1. Docker & Docker Compose (or Docker Desktop)
1. (Optional) `make` for convenience targets

## Quickstart — Local development

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

1. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

1. Run the app with Uvicorn (dev mode):

   ```bash
   python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

Open the interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Example endpoints:

- `GET /` — Hello world JSON
- `GET /items/{item_id}` — returns the path parameter and optional query

## Docker

Build and run locally (image exposes port 8000):

```bash
docker build -t fastapi-kong:local .
docker run --rm -p 8000:8000 fastapi-kong:local
```

## Docker Compose (app + Kong + Postgres)

Start the full stack (uses `docker-compose.yml`):

```bash
docker compose up --build
```

If your compose uses a database profile, example to start database-first:

```bash
KONG_DATABASE=postgres docker compose --profile database up -d
```

## Kong — Registering services and routes

Two options:

1. Register via Kong Admin API (imperative):

   ```bash
   # create a service pointing to the FastAPI container
   curl -i -X POST http://localhost:8001/services \
     --data name=fastapi-service \
     --data url='http://fastapi:8000/'

   # create a route that exposes the service at '/'
   curl -i -X POST http://localhost:8001/services/fastapi-service/routes \
     --data 'paths[]=/'
   ```

1. Use declarative configuration (DB-less Kong) — see `config/kong.yaml`.

Notes:

- Kong Admin API usually listens on port `8001` and the proxy on `8000` (verify your compose file).
- When using Docker Compose, service hostnames (e.g. `fastapi`) refer to container names in the same compose network.

## Configuration & secrets

- Copy `.env.example` -> `.env` and fill values before bringing up Compose.
- The repository includes a `POSTGRES_PASSWORD` file used by the compose setup — treat it as a secret and avoid committing real secrets to git.

## Makefile

Use `make` targets for common tasks:

- `make dev` — run uvicorn locally
- `make build` — docker build
- `make run` — build + run container
- `make compose-up` — docker compose up
- `make compose-down` — docker compose down (removes volumes/orphans)

Example:

```bash
make dev
```

## Testing

Run basic curl checks:

```bash
curl -i http://127.0.0.1:8000/
curl -i http://127.0.0.1:8000/items/5?q=foo
```

If Kong proxies `/`, call the proxy (adjust host/port as configured):

```bash
curl -i http://localhost:8000/ -H "Host: localhost"
```

## Troubleshooting

- If ports are in use, change the ports in `docker-compose.yml` and update Kong's target.
- Check container logs with `docker compose logs <service>`.
- For Kong DB errors, ensure Postgres is healthy and reachable by Kong (network & creds).

## Contributing

Contributions welcome — open an issue or submit a PR. Keep changes small and focused. Include tests where appropriate.

## License

Add a `LICENSE` file (for example: MIT) to make licensing explicit.

---

If you'd like, I can:

1. Add a short troubleshooting section specific to common Kong errors.
1. Add an example `docker-compose.override.yml` for development.
1. Add a short CI job to lint markdown and run a basic container smoke-test.

Tell me which you'd prefer and I'll implement it.
Two options:

1. Register via Kong Admin API (imperative):

   ```bash
   # create a service pointing to the FastAPI container
   curl -i -X POST http://localhost:8001/services \
     --data name=fastapi-service \
     --data url='http://fastapi:8000/'

   # create a route that exposes the service at '/'
   curl -i -X POST http://localhost:8001/services/fastapi-service/routes \
     --data 'paths[]=/'
   ```

1. Use declarative configuration (DB-less Kong) — see `config/kong.yaml`.

Notes:

- Kong Admin API usually listens on port `8001` and the proxy on `8000` (verify your compose file).
- When using Docker Compose, service hostnames (e.g. `fastapi`) refer to container names in the same compose network.

## Configuration & secrets

- Copy `.env.example` -> `.env` and fill values before bringing up Compose.
- The repository includes a `POSTGRES_PASSWORD` file used by the compose setup — treat it as a secret and avoid committing real secrets to git.

## Makefile

Use `make` targets for common tasks:

- `make dev` — run uvicorn locally
- `make build` — docker build
- `make run` — build + run container
- `make compose-up` — docker compose up
- `make compose-down` — docker compose down (removes volumes/orphans)

Example:

```bash
make dev
```

## Testing

Run basic curl checks:

```bash
curl -i http://127.0.0.1:8000/
curl -i http://127.0.0.1:8000/items/5?q=foo
```

If Kong proxies `/`, call the proxy (adjust host/port as configured):

```bash
curl -i http://localhost:8000/ -H "Host: localhost"
```

## Troubleshooting

- If ports are in use, change the ports in `docker-compose.yml` and update Kong's target.
- Check container logs with `docker compose logs <service>`.
- For Kong DB errors, ensure Postgres is healthy and reachable by Kong (network & creds).

## Contributing

Contributions welcome — open an issue or submit a PR. Keep changes small and focused. Include tests where appropriate.

## License

Add a `LICENSE` file (for example: MIT) to make licensing explicit.

---

If you'd like, I can:

1. Add a short troubleshooting section specific to common Kong errors.
1. Add an example `docker-compose.override.yml` for development.
1. Add a short CI job to lint markdown and run a basic container smoke-test.

Tell me which you'd prefer and I'll implement it.

