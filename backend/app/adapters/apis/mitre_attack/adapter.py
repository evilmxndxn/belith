from __future__ import annotations

from ....adapters.base import AdapterResponse
from .client import MitreAttackClient
from .schema import normalize


class MitreAttackAdapter:
    name = "mitre_attack"

    def __init__(self) -> None:
        self._client = MitreAttackClient()

    async def enrich(self, input_value: str) -> AdapterResponse:
        stix_bundle = await self._client.fetch_stix()
        entities, relationships = normalize(stix_bundle, input_value)
        return AdapterResponse(entities=entities, relationships=relationships, raw_metadata={"source": "mitre_attack"})
