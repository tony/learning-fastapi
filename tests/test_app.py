"""Tests for the FastAPI HTTP and GraphQL routes."""

from fastapi.testclient import TestClient
from starlette import status

from app import app

app.debug = True


def test_hello_world() -> None:
    """Return the HTTP greeting from the root route."""
    with TestClient(app=app) as client:
        response = client.get("/")
        assert response.status_code == status.HTTP_200_OK
        assert response.text == "Hello, world!"


def test_graphql_hello() -> None:
    """Resolve the GraphQL query for the default greeting."""
    with TestClient(app=app) as client:
        response = client.post(
            "/graphql",
            json={
                "query": r"""
query {
  hello
}""",
            },
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "data": {
                "hello": "Hello World",
            },
        }
