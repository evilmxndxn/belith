from __future__ import annotations

import httpx

from ....config.settings import settings
from .config import OpenPhishConfig


class OpenPhishClient:
    def __init__(self) -> None:
        self._config = OpenPhishConfig()

    async def fetch_feed(self) -> list[str]:
        async with httpx.AsyncClient(timeout=settings.request_timeout_s) as client:
            response = await client.get(settings.openphish_feed_url or self._config.feed_url)
            response.raise_for_status()
            return [line.strip() for line in response.text.splitlines() if line.strip()]
