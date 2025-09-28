from collections.abc import Callable, Sequence
from typing import Any, TypeVar

_F = TypeVar("_F", bound=Callable[..., Any])

class FastAPI:
    def __init__(self, **kwargs: Any) -> None: ...
    def include_router(self, router: Any, *, prefix: str = ...) -> None: ...
    def add_api_route(
        self,
        path: str,
        endpoint: Callable[..., Any],
        *,
        response_class: Any | None = ...,
        methods: Sequence[str] | None = ...,
    ) -> None: ...
    def get(self, path: str, **kwargs: Any) -> Callable[[_F], _F]: ...
