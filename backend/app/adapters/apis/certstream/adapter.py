from __future__ import annotations

from ....adapters.base import AdapterResponse
from .client import CertStreamClient
from .schema import normalize


class CertStreamAdapter:
    name = "certstream"

    def __init__(self) -> None:
        self._client = CertStreamClient()

    async def enrich(self, input_value: str) -> AdapterResponse:
        message = await self._client.listen_once()
        entities, relationships = normalize(message)
        return AdapterResponse(entities=entities, relationships=relationships, raw_metadata={"source": "certstream"})
