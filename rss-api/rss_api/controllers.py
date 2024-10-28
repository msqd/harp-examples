from typing import override

import feedparser

from harp.http import HttpResponse
from harp.views.json import serialize as json_serialize
from harp_apps.proxy.controllers import HttpProxyController, ProxyFilterResult
from harp_apps.proxy.events import ProxyFilterEvent


class FeedController(HttpProxyController):
    @override
    async def filter_request(self, context: ProxyFilterEvent) -> ProxyFilterResult:
        context = await super().filter_request(context)

        # we only handle GETs
        if context.request.method != "GET":
            return HttpResponse("Method not allowed.", status=405)

        # everything goes to archive.xml
        context.request.path = "/archive.xml"

    @override
    async def filter_response(self, context: ProxyFilterEvent) -> ProxyFilterEvent:
        context = await super().filter_response(context)
        initial_response = context.response

        # parse the xml feed into a python dict
        try:
            parsed_feed = feedparser.parse(initial_response.body)
        except Exception as e:
            context.response = HttpResponse(
                json_serialize({"error": str(e)}),
                status=500,
                content_type="application/json",
            )
            return context

        # convert the dict into a json string
        try:
            json_feed = json_serialize(parsed_feed)
        except Exception as e:
            context.response = HttpResponse(
                json_serialize({"error": str(e)}),
                status=500,
                content_type="application/json",
            )
            return context

        # job is done
        context.response = HttpResponse(json_feed, status=initial_response.status, content_type="application/json")
