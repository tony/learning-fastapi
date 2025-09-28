"""Application runner for local development and deployment."""

from __future__ import annotations

import uvicorn

from app.settings import settings


def run() -> None:
    """Launch the ASGI server with configured host/port defaults."""
    uvicorn.run(
        "app:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
    )


if __name__ == "__main__":
    run()
