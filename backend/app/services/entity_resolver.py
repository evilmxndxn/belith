from __future__ import annotations

from typing import Dict, Tuple, List

from ..models.entity import Entity, EntityType
from ..utils.normalizers import normalize_email, normalize_domain, normalize_ip


class EntityResolver:
    def __init__(self) -> None:
        self._entities: Dict[Tuple[EntityType, str], Entity] = {}

    def _key(self, e: Entity) -> Tuple[EntityType, str]:
        v = e.canonical_value
        if e.entity_type == EntityType.EMAIL:
            v = normalize_email(v)
        elif e.entity_type == EntityType.DOMAIN:
            v = normalize_domain(v)
        elif e.entity_type == EntityType.IP_ADDRESS:
            v = normalize_ip(v)
        return e.entity_type, v

    def upsert(self, entity: Entity) -> Entity:
        key = self._key(entity)
        existing = self._entities.get(key)
        if existing:
            # Simple merge: keep higher confidence and merge metadata
            if entity.confidence.value > existing.confidence.value:
                existing.confidence = entity.confidence
            existing.metadata.update(entity.metadata)
            return existing
        self._entities[key] = entity
        return entity

    def list_all(self) -> List[Entity]:
        return list(self._entities.values())
