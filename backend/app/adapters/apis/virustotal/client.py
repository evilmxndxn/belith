from __future__ import annotations

import base64
import httpx

from ....config.settings import settings
from .config import VirusTotalConfig


class VirusTotalClient:
    def __init__(self) -> None:
        self._config = VirusTotalConfig()

    async def fetch(self, endpoint: str) -> dict:
        headers = {"x-apikey": settings.virustotal_key} if settings.virustotal_key else {}
        async with httpx.AsyncClient(timeout=settings.request_timeout_s) as client:
            response = await client.get(f"{self._config.base_url}/{endpoint}", headers=headers)
            response.raise_for_status()
            return response.json()

    async def lookup(self, input_value: str) -> dict:
        if "://" in input_value:
            url_id = base64.urlsafe_b64encode(input_value.encode()).decode().strip("=")
            return await self.fetch(f"urls/{url_id}")
        if "." in input_value and not input_value.replace(".", "").isdigit():
            return await self.fetch(f"domains/{input_value}")
        if ":" in input_value or input_value.count(".") == 3:
            return await self.fetch(f"ip_addresses/{input_value}")
        return await self.fetch(f"files/{input_value}")
