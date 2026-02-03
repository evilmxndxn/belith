from __future__ import annotations

import httpx

from ....config.settings import settings
from .config import GreyNoiseConfig


class GreyNoiseClient:
    def __init__(self) -> None:
        self._config = GreyNoiseConfig()

    async def context(self, ip: str) -> dict:
        headers = {"key": settings.greynoise_key} if settings.greynoise_key else {}
        async with httpx.AsyncClient(timeout=settings.request_timeout_s) as client:
            response = await client.get(f"{self._config.base_url}/v3/community/{ip}", headers=headers)
            response.raise_for_status()
            return response.json()
