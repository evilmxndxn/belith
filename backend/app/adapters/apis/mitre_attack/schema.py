from __future__ import annotations

from typing import List

from ....models.entity import Entity, EntityType, Relationship
from ....utils.normalization import build_entity, build_relationship


def normalize(stix_bundle: dict, query: str) -> tuple[list[Entity], list[Relationship]]:
    objects = stix_bundle.get("objects", [])
    entities: List[Entity] = []
    relationships: List[Relationship] = []
    query_lower = query.lower()

    for obj in objects:
        if obj.get("type") == "attack-pattern" and query_lower in obj.get("name", "").lower():
            technique_entity = build_entity(
                EntityType.technique,
                obj.get("name"),
                "mitre_attack",
                "api",
                0.6,
                {"external_id": _external_id(obj), "description": obj.get("description")},
            )
            entities.append(technique_entity)
        if obj.get("type") == "intrusion-set" and query_lower in obj.get("name", "").lower():
            actor_entity = build_entity(EntityType.threat_actor, obj.get("name"), "mitre_attack", "api", 0.6, {})
            entities.append(actor_entity)

    for obj in objects:
        if obj.get("type") == "relationship" and obj.get("relationship_type") == "uses":
            source_ref = obj.get("source_ref")
            target_ref = obj.get("target_ref")
            source_entity = _entity_by_ref(entities, source_ref)
            target_entity = _entity_by_ref(entities, target_ref)
            if source_entity and target_entity:
                relationships.append(build_relationship(source_entity, target_entity, "uses", 0.5, source_entity.sources))

    return entities, relationships


def _external_id(obj: dict) -> str | None:
    for ref in obj.get("external_references", []):
        if ref.get("source_name") == "mitre-attack":
            return ref.get("external_id")
    return None


def _entity_by_ref(entities: list[Entity], ref: str | None) -> Entity | None:
    if not ref:
        return None
    for entity in entities:
        if ref.lower() in entity.value.lower():
            return entity
    return None
