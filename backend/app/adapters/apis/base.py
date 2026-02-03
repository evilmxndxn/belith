from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

import httpx

from ...core.rate_limit import get_bucket
from ...models.entity import Entity, EntitySource, SourceType
from ...models.relationship import Relationship


class BaseAPIAdapter(ABC):
    name: str
    rate_per_sec: float = 1.0
    capacity: int = 5

    def __init__(self) -> None:
        self._bucket = get_bucket(self.name, self.rate_per_sec, self.capacity)

    async def _client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(timeout=10.0)

    async def _acquire(self) -> None:
        if not self._bucket.consume():
            raise RuntimeError(f"Rate limit exceeded for adapter {self.name}")

    @abstractmethod
    async def execute(self, entities: List[Entity]) -> List[Entity | Relationship]:
        ...

    @staticmethod
    def source() -> EntitySource:
        return EntitySource(name="unknown_api", type=SourceType.API)
