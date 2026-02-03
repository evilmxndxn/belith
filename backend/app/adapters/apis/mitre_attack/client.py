from __future__ import annotations

import httpx

from ....config.settings import settings
from .config import MitreAttackConfig


class MitreAttackClient:
    def __init__(self) -> None:
        self._config = MitreAttackConfig()

    async def fetch_stix(self) -> dict:
        async with httpx.AsyncClient(timeout=settings.request_timeout_s) as client:
            response = await client.get(self._config.stix_url)
            response.raise_for_status()
            return response.json()
