## Learning FastAPI

This repository contains a minimal FastAPI application with a REST endpoint and a Strawberry-powered GraphQL endpoint. It is intended as a playground for experimenting with FastAPI, Strawberry GraphQL, and the surrounding tooling (uv, pytest, mypy, and ruff).

### Useful Commands

- `uv sync --all-extras --dev --upgrade` – install and refresh dependencies
- `uv run uvicorn app:app --host 127.0.0.1 --port 8020` – start the development server
- `uv run py.test` – execute the test suite
- `uv run mypy` – run strict static type checks
- `uv run ruff check --select ALL . --fix --unsafe-fixes --preview --show-fixes` – apply lint fixes
- `uv run ruff format .` – format the codebase
- `uv run python -m app.server` – alternative launcher using environment overrides
- Add environment overrides in `.env` (e.g. `APP_PORT=8020`, `APP_RELOAD=true`)
