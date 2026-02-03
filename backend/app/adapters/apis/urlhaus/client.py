from __future__ import annotations

import httpx

from ....config.settings import settings
from .config import UrlHausConfig


class UrlHausClient:
    def __init__(self) -> None:
        self._config = UrlHausConfig()

    async def lookup_url(self, url: str) -> dict:
        async with httpx.AsyncClient(timeout=settings.request_timeout_s) as client:
            response = await client.post(f"{self._config.base_url}/url/", data={"url": url})
            response.raise_for_status()
            return response.json()

    async def lookup_host(self, host: str) -> dict:
        async with httpx.AsyncClient(timeout=settings.request_timeout_s) as client:
            response = await client.post(f"{self._config.base_url}/host/", data={"host": host})
            response.raise_for_status()
            return response.json()
