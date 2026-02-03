from __future__ import annotations

from typing import Dict

from ..models.entity import Entity, EntitySource, EntityType, Relationship
from .hashing import stable_id
from .time import utc_now


def build_entity(
    entity_type: EntityType,
    value: str,
    source_name: str,
    source_type: str,
    confidence: float,
    metadata: Dict[str, str | int | float | bool | None] | None = None,
    reference_url: str | None = None,
) -> Entity:
    return Entity(
        id=stable_id(entity_type.value, value, source_name),
        type=entity_type,
        value=value,
        sources=[EntitySource(name=source_name, source_type=source_type, confidence=confidence, reference_url=reference_url)],
        timestamp=utc_now(),
        confidence=confidence,
        metadata=metadata or {},
    )


def build_relationship(
    source: Entity,
    target: Entity,
    relationship_type: str,
    confidence: float,
    provenance: list[EntitySource],
    metadata: Dict[str, str | int | float | bool | None] | None = None,
) -> Relationship:
    return Relationship(
        id=stable_id(source.id, target.id, relationship_type),
        source_id=source.id,
        target_id=target.id,
        relationship_type=relationship_type,
        confidence=confidence,
        provenance=provenance,
        metadata=metadata or {},
    )
