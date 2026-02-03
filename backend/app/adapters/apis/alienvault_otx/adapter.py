from __future__ import annotations

from ....adapters.base import AdapterResponse
from .client import AlienVaultOtxClient
from .schema import normalize


class AlienVaultOtxAdapter:
    name = "alienvault_otx"

    def __init__(self) -> None:
        self._client = AlienVaultOtxClient()

    async def enrich(self, input_value: str) -> AdapterResponse:
        response = await self._client.indicators(input_value)
        entities, relationships = normalize(response, input_value)
        return AdapterResponse(entities=entities, relationships=relationships, raw_metadata={"source": "alienvault_otx"})
