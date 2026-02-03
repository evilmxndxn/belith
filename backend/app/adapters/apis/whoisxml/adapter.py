from __future__ import annotations

from ....adapters.base import AdapterResponse
from .client import WhoisXmlClient
from .schema import normalize


class WhoisXmlAdapter:
    name = "whoisxml"

    def __init__(self) -> None:
        self._client = WhoisXmlClient()

    async def enrich(self, input_value: str) -> AdapterResponse:
        response = await self._client.lookup(input_value)
        entities, relationships = normalize(response, input_value)
        return AdapterResponse(entities=entities, relationships=relationships, raw_metadata={"source": "whoisxml"})
