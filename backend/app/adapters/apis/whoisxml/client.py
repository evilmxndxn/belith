from __future__ import annotations

import httpx

from ....config.settings import settings
from .config import WhoisXmlConfig


class WhoisXmlClient:
    def __init__(self) -> None:
        self._config = WhoisXmlConfig()

    async def lookup(self, domain: str) -> dict:
        params = {
            "apiKey": settings.whoisxml_key,
            "domainName": domain,
            "outputFormat": "JSON",
        }
        async with httpx.AsyncClient(timeout=settings.request_timeout_s) as client:
            response = await client.get(self._config.base_url, params=params)
            response.raise_for_status()
            return response.json()
