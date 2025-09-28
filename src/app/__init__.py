"""Application entrypoints for HTTP and GraphQL routes."""

import strawberry
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from strawberry import Private
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Query:
    """Root GraphQL query type."""

    greeting: Private[str] = "Hello World"

    @strawberry.field
    def hello(self) -> str:
        """Return the configured greeting.

        Returns
        -------
        str
            Greeting configured for GraphQL responses.
        """
        return self.greeting


schema = strawberry.Schema(Query)

# GraphQL router mounts the schema at /graphql with a lightweight root factory.
graphql_router = GraphQLRouter(
    schema,
    path="/graphql",
    root_value_getter=Query,
)

app = FastAPI()


@app.get(
    "/",
    response_class=PlainTextResponse,
)
def hello_world() -> str:
    """Return a greeting for the HTTP route.

    Returns
    -------
    str
        Plain-text greeting for the FastAPI response.
    """
    return "Hello, world!"


app.include_router(graphql_router)
