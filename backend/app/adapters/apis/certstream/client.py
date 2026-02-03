from __future__ import annotations

import asyncio
import json

import websockets

from ....config.settings import settings
from .config import CertStreamConfig


class CertStreamClient:
    def __init__(self) -> None:
        self._config = CertStreamConfig()

    async def listen_once(self) -> dict:
        ws_url = settings.certstream_ws_url or self._config.ws_url
        async with websockets.connect(ws_url) as websocket:
            try:
                message = await asyncio.wait_for(websocket.recv(), timeout=settings.request_timeout_s)
            except asyncio.TimeoutError:
                return {"message_type": "timeout"}
        return json.loads(message)
