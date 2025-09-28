from typing import Any

class PlainTextResponse:
    media_type: str

    def __init__(
        self,
        content: str = ...,
        status_code: int | None = ...,
        headers: dict[str, str] | None = ...,
        media_type: str | None = ...,
        background: Any = ...,
    ) -> None: ...
