from asyncio import gather
from functools import partial
from harp import __revision__, __version__, get_logger

from harp.controllers import (
    ProxyControllerResolver,
)

import orjson
from .settings import AggregateSettings, AgregatorSettings
from harp.http import HttpRequest, HttpResponse

logger = get_logger(__name__)


class AggregatorController:

    def __init__(
        self,
        *,
        resolver: ProxyControllerResolver,
        settings: AgregatorSettings,
    ):

        self.resolver = resolver
        self.aggregates = settings.aggregates
        self.path_to_aggregate = {
            aggregate.path: partial(self._handle_for_aggregate, aggregate=aggregate)
            for aggregate in self.aggregates
        }

    def find_handler_for_request(self, request: HttpRequest):
        return self.path_to_aggregate.get(request.path)

    async def _handle_for_aggregate(
        self, request: HttpRequest, aggregate: AggregateSettings
    ):
        requests = []
        for endpoint in aggregate.endpoints:
            endpoint_object = self.resolver.endpoints.get(endpoint.name)
            server_port = endpoint_object.settings.port if endpoint_object else None
            request = HttpRequest(
                method=aggregate.method,
                path=endpoint.path,
                server_port=server_port,
                headers=request.headers,
            )
            requests.append(request)

        # send requests
        controllers = await gather(
            *[self.resolver.resolve(request) for request in requests]
        )

        responses = await gather(
            *[controller(request) for controller, request in zip(controllers, requests)]
        )

        # Merge responses into a single response
        content = {}
        for response in responses:
            response_body = orjson.loads(response.body)
            content.update(response_body)

        return HttpResponse(orjson.dumps(content))

    async def __call__(self, request: HttpRequest):
        handler = self.find_handler_for_request(request)
        if handler:
            return await handler(request)
        else:
            return HttpResponse("Could not find a handler for this request", status=404)
