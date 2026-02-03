from __future__ import annotations

from ....adapters.base import AdapterResponse
from .client import ShodanClient
from .schema import normalize_domain, normalize_host


class ShodanAdapter:
    name = "shodan"

    def __init__(self) -> None:
        self._client = ShodanClient()

    async def enrich(self, input_value: str) -> AdapterResponse:
        if "." in input_value and not input_value.replace(".", "").isdigit():
            response = await self._client.domain(input_value)
            entities, relationships = normalize_domain(response, input_value)
        else:
            response = await self._client.host(input_value)
            entities, relationships = normalize_host(response, input_value)
        return AdapterResponse(entities=entities, relationships=relationships, raw_metadata={"source": "shodan"})
