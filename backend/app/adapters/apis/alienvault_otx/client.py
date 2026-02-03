from __future__ import annotations

import httpx

from ....config.settings import settings
from .config import AlienVaultOtxConfig


class AlienVaultOtxClient:
    def __init__(self) -> None:
        self._config = AlienVaultOtxConfig()

    async def indicators(self, input_value: str) -> dict:
        headers = {"X-OTX-API-KEY": settings.alienvault_key} if settings.alienvault_key else {}
        if "." in input_value and not input_value.replace(".", "").isdigit():
            endpoint = f"indicators/domain/{input_value}/general"
        elif ":" in input_value or input_value.count(".") == 3:
            endpoint = f"indicators/IPv4/{input_value}/general"
        else:
            endpoint = f"indicators/file/{input_value}/general"
        async with httpx.AsyncClient(timeout=settings.request_timeout_s) as client:
            response = await client.get(f"{self._config.base_url}/{endpoint}", headers=headers)
            response.raise_for_status()
            return response.json()
