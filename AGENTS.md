# AGENTS.md

learning-fastapi is a personal playground for FastAPI's REST routing next
to Strawberry GraphQL: one HTTP route, one GraphQL query, tested with
pytest and FastAPI's `TestClient`.

Follow the conventions already in the tree, and keep a change scoped to
what was asked for.

## What is here

| Path                            | What it is                                                                       |
| -------------------------------- | ---------------------------------------------------------------------------------- |
| `src/app/app.py`                | FastAPI app: `GET /` route, `POST /graphql` Strawberry router, `run()` entry point |
| `src/app/settings.py`           | `Settings` (host, port, reload) read from `APP_`-prefixed env vars              |
| `src/app/__init__.py`           | Re-exports `app` and `run` for `uvicorn app:app`                                |
| `tests/test_app.py`             | HTTP and GraphQL integration tests via `TestClient`                             |
| `.github/workflows/tests.yml`   | CI: ruff check, ruff format --check, mypy, pytest                               |
| `pyproject.toml`                | Dependencies; ruff, mypy, and pytest configuration                              |

## Which policy applies

- Documentation, user-facing text, commit messages, docstrings, and
  source comments: [.github/WRITING.md](.github/WRITING.md)
- Environment, the gates, tests, and pull requests:
  [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md)

Each of those is the single home for its subject. Where a rule seems to
be stated twice, the file listed above is the one that governs.

## Change discipline

- Make the smallest coherent change that solves the verified problem;
  keep unrelated cleanup out of it.
- Reuse an existing file, helper, API, or test before adding a new one.
- Add a file only for a durable boundary — a distinct responsibility,
  independent reuse, or splitting an oversized module — not for a
  single-use helper or a one-line re-export.
- Add a test for every user-visible behaviour change.
- A passing gate is evidence only once it has been shown capable of
  failing. Pair a new test with a deliberate break that proves it bites.

Pytest configuration lives in `[tool.pytest]` using pytest 9's
native-TOML mode, not the older `[tool.pytest.ini_options]` string mode
— the two are mutually exclusive in one `pyproject.toml`, so do not add
the second form alongside the first.

## References

- [FastAPI](https://fastapi.tiangolo.com)
- [Strawberry GraphQL](https://strawberry.rocks)
- [uv](https://github.com/astral-sh/uv)
