from __future__ import annotations

from typing import List

from bs4 import BeautifulSoup  # requires bs4 in requirements if used
import httpx

from ...models.entity import Entity, EntityType, EntitySource, SourceType
from ...models.relationship import Relationship, RelationshipType
from ...models.confidence import ConfidenceScore
from ...core.rate_limit import get_bucket


class AhmiaAdapter:
    name = "ahmia"
    rate_per_sec = 0.5
    capacity = 2

    def __init__(self) -> None:
        self._bucket = get_bucket(self.name, self.rate_per_sec, self.capacity)

    @staticmethod
    def source() -> EntitySource:
        return EntitySource(name="ahmia", type=SourceType.API)

    async def execute(self, entities: List[Entity]) -> List[Entity | Relationship]:
        results: List[Entity | Relationship] = []
        async with httpx.AsyncClient(timeout=10.0) as client:
            for e in entities:
                if e.entity_type not in {EntityType.USERNAME, EntityType.DOMAIN, EntityType.NOTE}:
                    continue
                if not self._bucket.consume():
                    break
                query = e.canonical_value
                resp = await client.get(f"https://ahmia.fi/search/?q={query}")
                if resp.status_code != 200:
                    continue
                soup = BeautifulSoup(resp.text, "html.parser")
                for link in soup.select("a"):
                    href = link.get("href", "")
                    if ".onion" in href:
                        onion = href.strip()
                        new_entity = Entity(
                            entity_type=EntityType.DOMAIN,
                            canonical_value=onion,
                            source=self.source(),
                            confidence=ConfidenceScore(value=0.6, rationale="Found in Ahmia search"),
                        )
                        rel = Relationship(
                            from_entity_id=e.id,
                            to_entity_id=new_entity.id,
                            relationship_type=RelationshipType.ASSOCIATED_WITH,
                            source=self.source(),
                            confidence=ConfidenceScore(value=0.6),
                        )
                        results.append(new_entity)
                        results.append(rel)
        return results
