from __future__ import annotations

import httpx

from ....config.settings import settings
from .config import PhishTankConfig


class PhishTankClient:
    def __init__(self) -> None:
        self._config = PhishTankConfig()

    async def check(self, url: str) -> dict:
        data = {
            "url": url,
            "format": "json",
            "app_key": settings.phishtank_key or "",
        }
        async with httpx.AsyncClient(timeout=settings.request_timeout_s) as client:
            response = await client.post(self._config.base_url, data=data)
            response.raise_for_status()
            return response.json()
