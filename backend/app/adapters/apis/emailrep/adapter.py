from __future__ import annotations

from typing import List

import httpx

from ...config.settings import settings
from ...models.entity import Entity, EntityType, EntitySource, SourceType
from ...models.confidence import ConfidenceScore
from ...models.relationship import Relationship, RelationshipType
from ...core.rate_limit import get_bucket


class EmailRepAdapter:
    name = "emailrep"
    rate_per_sec = 1.0
    capacity = 5
    base_url = "https://emailrep.io"

    def __init__(self) -> None:
        self._bucket = get_bucket(self.name, self.rate_per_sec, self.capacity)

    @staticmethod
    def source() -> EntitySource:
        return EntitySource(name="emailrep", type=SourceType.API)

    async def execute(self, entities: List[Entity]) -> List[Entity | Relationship]:
        results: List[Entity | Relationship] = []
        headers = {}
        if settings.emailrep_api_key:
            headers["Key"] = settings.emailrep_api_key

        async with httpx.AsyncClient(timeout=10.0, headers=headers) as client:
            for e in entities:
                if e.entity_type != EntityType.EMAIL:
                    continue
                if not self._bucket.consume():
                    break
                resp = await client.get(f"{self.base_url}/{e.canonical_value}")
                if resp.status_code != 200:
                    continue
                data = resp.json()
                risk = data.get("reputation", "unknown")
                score = 0.5
                if risk == "high":
                    score = 0.9
                elif risk == "medium":
                    score = 0.7
                elif risk == "low":
                    score = 0.3
                e.metadata["emailrep"] = data
                e.confidence = ConfidenceScore(value=min(1.0, e.confidence.value + 0.1))
                results.append(e)
        return results
