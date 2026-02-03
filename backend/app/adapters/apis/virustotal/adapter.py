from __future__ import annotations

from ....adapters.base import AdapterResponse
from .client import VirusTotalClient
from .schema import normalize


class VirusTotalAdapter:
    name = "virustotal"

    def __init__(self) -> None:
        self._client = VirusTotalClient()

    async def enrich(self, input_value: str) -> AdapterResponse:
        response = await self._client.lookup(input_value)
        entities, relationships = normalize(response, input_value)
        return AdapterResponse(entities=entities, relationships=relationships, raw_metadata={"source": "virustotal"})
