from __future__ import annotations

from typing import List
import json
import os
import tempfile

from ...models.entity import Entity, EntityType, EntitySource, SourceType
from ...models.relationship import Relationship, RelationshipType
from ...models.confidence import ConfidenceScore
from .base import BaseToolAdapter


class SherlockAdapter(BaseToolAdapter):
    name = "sherlock"
    requires_active_scanning = True

    @staticmethod
    def source() -> EntitySource:
        return EntitySource(name="sherlock", type=SourceType.TOOL)

    async def execute(self, entities: List[Entity]) -> List[Entity | Relationship]:
        results: List[Entity | Relationship] = []
        usernames = [e for e in entities if e.entity_type == EntityType.USERNAME]
        if not usernames:
            return results

        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = os.path.join(tmpdir, "sherlock.json")
            # Run sherlock once per username for simplicity
            for e in usernames:
                cmd = f"sherlock {e.canonical_value} --print-found --json {out_file}"
                stdout = await self._run_command(cmd, timeout=300)
                _ = stdout  # not used; results in file
                if not os.path.exists(out_file):
                    continue
                with open(out_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                for site, info in data.items():
                    if not info.get("exists"):
                        continue
                    url = info.get("url_main") or info.get("url_user")
                    account_entity = Entity(
                        entity_type=EntityType.ACCOUNT_ID,
                        canonical_value=f"{site}:{e.canonical_value}",
                        source=self.source(),
                        confidence=ConfidenceScore(value=0.8, rationale="Sherlock found account"),
                        metadata={"url": url},
                    )
                    rel = Relationship(
                        from_entity_id=e.id,
                        to_entity_id=account_entity.id,
                        relationship_type=RelationshipType.ASSOCIATED_WITH,
                        source=self.source(),
                        confidence=ConfidenceScore(value=0.8),
                    )
                    results.append(account_entity)
                    results.append(rel)
        return results
