from __future__ import annotations

from ....adapters.base import AdapterResponse
from .client import OpenPhishClient
from .schema import normalize


class OpenPhishAdapter:
    name = "openphish"

    def __init__(self) -> None:
        self._client = OpenPhishClient()

    async def enrich(self, input_value: str) -> AdapterResponse:
        feed = await self._client.fetch_feed()
        entities, relationships = normalize(feed, input_value)
        return AdapterResponse(entities=entities, relationships=relationships, raw_metadata={"source": "openphish"})
