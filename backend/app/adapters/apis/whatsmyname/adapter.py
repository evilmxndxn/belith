from __future__ import annotations

from typing import List, Dict, Any
from uuid import uuid4

import httpx

from ...models.entity import Entity, EntityType, EntitySource, SourceType
from ...models.relationship import Relationship, RelationshipType
from ...models.confidence import ConfidenceScore
from ...core.rate_limit import get_bucket


class WhatsMyNameAdapter:
    name = "whatsmyname"
    rate_per_sec = 0.2
    capacity = 1
    data_url = "https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json"

    def __init__(self) -> None:
        self._bucket = get_bucket(self.name, self.rate_per_sec, self.capacity)
        self._sites: List[Dict[str, Any]] = []

    @staticmethod
    def source() -> EntitySource:
        return EntitySource(name="whatsmyname", type=SourceType.API)

    async def _load_sites(self) -> None:
        if self._sites:
            return
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(self.data_url)
            resp.raise_for_status()
            data = resp.json()
            self._sites = data.get("sites", [])

    async def execute(self, entities: List[Entity]) -> List[Entity | Relationship]:
        await self._load_sites()
        results: List[Entity | Relationship] = []
        async with httpx.AsyncClient(timeout=10.0) as client:
            for e in entities:
                if e.entity_type != EntityType.USERNAME:
                    continue
                if not self._bucket.consume():
                    break
                username = e.canonical_value
                for site in self._sites[:20]:  # limit for demo
                    url = site.get("uri_check", "").replace("{account}", username)
                    if not url:
                        continue
                    try:
                        resp = await client.get(url, follow_redirects=True)
                    except Exception:
                        continue
                    if resp.status_code == 200:
                        account_entity = Entity(
                            entity_type=EntityType.ACCOUNT_ID,
                            canonical_value=f"{site.get('name')}:{username}",
                            source=self.source(),
                            confidence=ConfidenceScore(value=0.7, rationale="Profile page returned 200"),
                            metadata={"url": url},
                        )
                        rel = Relationship(
                            from_entity_id=e.id,
                            to_entity_id=account_entity.id,
                            relationship_type=RelationshipType.ASSOCIATED_WITH,
                            source=self.source(),
                            confidence=ConfidenceScore(value=0.7),
                        )
                        results.append(account_entity)
                        results.append(rel)
        return results
