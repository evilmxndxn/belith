from __future__ import annotations

from collections import defaultdict
from typing import Iterable, List

from ..models.entity import Entity, EntitySource, Relationship


class FusionEngine:
    def __init__(self) -> None:
        self._entities: dict[str, Entity] = {}
        self._relationships: dict[str, Relationship] = {}

    async def ingest_entities(self, entities: Iterable[Entity]) -> List[Entity]:
        for entity in entities:
            self._merge_entity(entity)
        return list(self._entities.values())

    def ingest_relationships(self, relationships: Iterable[Relationship]) -> List[Relationship]:
        for relationship in relationships:
            self._merge_relationship(relationship)
        return list(self._relationships.values())

    def _merge_entity(self, entity: Entity) -> None:
        key = f"{entity.type}:{entity.value}"
        if key not in self._entities:
            self._entities[key] = entity
            return

        existing = self._entities[key]
        merged_sources = _merge_sources(existing.sources, entity.sources)
        existing.sources = merged_sources
        existing.confidence = _combine_confidence(existing.confidence, entity.confidence, merged_sources)
        existing.metadata.update(entity.metadata)

    def _merge_relationship(self, relationship: Relationship) -> None:
        if relationship.id not in self._relationships:
            self._relationships[relationship.id] = relationship
            return
        existing = self._relationships[relationship.id]
        existing.provenance = _merge_sources(existing.provenance, relationship.provenance)
        existing.confidence = _combine_confidence(existing.confidence, relationship.confidence, existing.provenance)
        existing.metadata.update(relationship.metadata)


def _merge_sources(existing: list[EntitySource], incoming: list[EntitySource]) -> list[EntitySource]:
    merged = {source.name: source for source in existing}
    for source in incoming:
        merged[source.name] = source
    return list(merged.values())


def _combine_confidence(base: float, incoming: float, sources: list[EntitySource]) -> float:
    if len(sources) <= 1:
        return max(base, incoming)
    combined = min(1.0, base + incoming * 0.25)
    return max(combined, 0.1)
