from __future__ import annotations

from ....adapters.base import AdapterResponse
from ..http_adapter import HttpAdapterClient, HttpAdapterConfig, normalize_http_response
from .config import AxolotlApiConfig


class AxolotlApiAdapter:
    name = "axolotl_api"

    def __init__(self) -> None:
        cfg = AxolotlApiConfig()
        self._config = HttpAdapterConfig(
            name=self.name,
            base_url=cfg.base_url,
            endpoint=cfg.endpoint,
            method="GET",
            auth_type=None,
            auth_in=None,
            auth_param=None,
            rate_limit=cfg.rate_limit,
            website=cfg.website,
            notes=cfg.notes,
        )
        self._client = HttpAdapterClient(self._config)

    async def enrich(self, input_value: str) -> AdapterResponse:
        payload = await self._client.request(input_value)
        entities, relationships = normalize_http_response(self._config, input_value, payload)
        return AdapterResponse(entities=entities, relationships=relationships, raw_metadata={"source": self.name})
