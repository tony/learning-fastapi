# Contributing

Thanks for looking. This is a personal FastAPI and Strawberry GraphQL
learning project — there is no roadmap, but a bug report with a
reproduction, or a note on where the documentation misled you, is
welcome.

How this project writes prose — README, commit messages, docstrings, and
source comments — is set out separately in [WRITING.md](WRITING.md). Read
that before changing any of it. The constraints every change is held to,
and the map of what is where, are in [AGENTS.md](../AGENTS.md).

## Getting set up

```console
$ uv sync --all-extras --dev
```

Add a runtime dependency:

```console
$ uv add <package>
```

Add a dev-only dependency:

```console
$ uv add --dev <package>
```

## The gates

CI ([.github/workflows/tests.yml](workflows/tests.yml)) runs these four,
in order; all four have to pass before a change is done.

Lint:

```console
$ uv run ruff check .
```

Format:

```console
$ uv run ruff format . --check
```

Type-check:

```console
$ uv run mypy .
```

Test:

```console
$ uv run pytest
```

A broader, non-CI ruff pass is available for a local deep audit. It
turns on every rule ruff ships, including preview rules, and applies
unsafe fixes, so review the diff before committing — this is not a gate
and CI does not run it:

```console
$ uv run ruff check --select ALL . --fix --unsafe-fixes --preview --show-fixes
```

Documentation is a gate, not a courtesy. Examples in docstrings under
`src/` and `tests/` are executed by `pytest` via `--doctest-modules`;
the doctest flags live in `pyproject.toml`, so there is no separate
doctest step and a green `pytest` is the proof. `README.md` is not in
`testpaths`, so nothing there is doctested. Which blocks qualify,
and the one mistake that silently removes a test, are in
[WRITING.md](WRITING.md#documented-examples-that-run).

Before claiming a test or a gate works, show it failing. A gate that has
never been red is an assumption.

## Tests

The suite is `pytest` with FastAPI's `TestClient` (a Starlette wrapper)
driving both the HTTP route and the GraphQL resolver in-process — no
external services, no fixtures beyond pytest's own, no markers.

Run a single test:

```console
$ uv run pytest tests/test_app.py::test_hello_world
```

Watch mode, rerunning on save:

```console
$ uv run pytest-watcher
```

## Pull requests

One subject per pull request. Unrelated cleanup found along the way
belongs in its own commit, and usually in its own pull request.

Discuss a substantial change via an issue before making it.

Commit format is in [WRITING.md](WRITING.md#commits).

## Decorum

- Participants will be tolerant of opposing views.
- Participants must ensure that their language and actions are free of
  personal attacks and disparaging personal remarks.
- When interpreting the words and actions of others, participants should
  always assume good intentions.
- Behaviour which can be reasonably considered harassment will not be
  tolerated.

Based on [Ruby's Community Conduct Guideline](https://www.ruby-lang.org/en/conduct/).

## Security

Please do not open a public issue for a vulnerability. Use GitHub's
private vulnerability reporting (the Security tab's "Report a
vulnerability" button) instead.
