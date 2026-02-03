from __future__ import annotations

from typing import List

from ..models.entity import Entity
from ..services.entity_resolver import EntityResolver
from ..services.task_engine import TaskEngine


class FusionEngine:
    def __init__(self) -> None:
        self.resolver = EntityResolver()
        self.tasks = TaskEngine()

    async def ingest_entities(self, entities: List[Entity]) -> List[Entity]:
        # Upsert initial entities
        for e in entities:
            self.resolver.upsert(e)
        # Run adapters
        new_entities = await self.tasks.run_for_entities(entities)
        for e in new_entities:
            self.resolver.upsert(e)
        return self.resolver.list_all()
