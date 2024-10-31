from pydantic import Field

from harp.config import Configurable


class Endpoint(Configurable):
    name: str
    path: str


class AggregateSettings(Configurable):
    path: str
    endpoints: list[Endpoint]
    method: str = Field(
        "GET", description="HTTP method to use when querying the endpoint."
    )


class AgregatorSettings(Configurable):
    """Root settings for the aggregator application."""

    port: int = Field(
        4080,
        description="Port on which the application will run.",
    )

    aggregates: list[AggregateSettings] = []
