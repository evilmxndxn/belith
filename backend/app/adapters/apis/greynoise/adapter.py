from __future__ import annotations

from ....adapters.base import AdapterResponse
from .client import GreyNoiseClient
from .schema import normalize


class GreyNoiseAdapter:
    name = "greynoise"

    def __init__(self) -> None:
        self._client = GreyNoiseClient()

    async def enrich(self, input_value: str) -> AdapterResponse:
        response = await self._client.context(input_value)
        entities, relationships = normalize(response, input_value)
        return AdapterResponse(entities=entities, relationships=relationships, raw_metadata={"source": "greynoise"})
