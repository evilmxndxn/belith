from __future__ import annotations

import httpx

from ....config.settings import settings
from .config import AbuseIpdbConfig


class AbuseIpdbClient:
    def __init__(self) -> None:
        self._config = AbuseIpdbConfig()

    async def check(self, ip: str) -> dict:
        headers = {"Key": settings.abuseipdb_key, "Accept": "application/json"} if settings.abuseipdb_key else {"Accept": "application/json"}
        params = {"ipAddress": ip, "maxAgeInDays": 90}
        async with httpx.AsyncClient(timeout=settings.request_timeout_s) as client:
            response = await client.get(f"{self._config.base_url}/check", params=params, headers=headers)
            response.raise_for_status()
            return response.json()
