from __future__ import annotations

from ....adapters.base import AdapterResponse
from .client import PhishTankClient
from .schema import normalize


class PhishTankAdapter:
    name = "phishtank"

    def __init__(self) -> None:
        self._client = PhishTankClient()

    async def enrich(self, input_value: str) -> AdapterResponse:
        response = await self._client.check(input_value)
        entities, relationships = normalize(response, input_value)
        return AdapterResponse(entities=entities, relationships=relationships, raw_metadata={"source": "phishtank"})
