from __future__ import annotations

from ....adapters.base import AdapterResponse
from .client import UrlHausClient
from .schema import normalize_host, normalize_url


class UrlHausAdapter:
    name = "urlhaus"

    def __init__(self) -> None:
        self._client = UrlHausClient()

    async def enrich(self, input_value: str) -> AdapterResponse:
        if "://" in input_value:
            response = await self._client.lookup_url(input_value)
            entities, relationships = normalize_url(response, input_value)
        else:
            response = await self._client.lookup_host(input_value)
            entities, relationships = normalize_host(response, input_value)
        return AdapterResponse(entities=entities, relationships=relationships, raw_metadata={"source": "urlhaus"})
