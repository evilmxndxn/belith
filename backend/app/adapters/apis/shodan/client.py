from __future__ import annotations

import httpx

from ....config.settings import settings
from .config import ShodanConfig


class ShodanClient:
    def __init__(self) -> None:
        self._config = ShodanConfig()

    async def host(self, ip: str) -> dict:
        params = {"key": settings.shodan_key} if settings.shodan_key else {}
        async with httpx.AsyncClient(timeout=settings.request_timeout_s) as client:
            response = await client.get(f"{self._config.base_url}/shodan/host/{ip}", params=params)
            response.raise_for_status()
            return response.json()

    async def domain(self, domain: str) -> dict:
        params = {"key": settings.shodan_key} if settings.shodan_key else {}
        async with httpx.AsyncClient(timeout=settings.request_timeout_s) as client:
            response = await client.get(f"{self._config.base_url}/dns/domain/{domain}", params=params)
            response.raise_for_status()
            return response.json()
