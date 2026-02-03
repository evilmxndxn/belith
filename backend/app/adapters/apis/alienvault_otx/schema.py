from __future__ import annotations

from typing import List

from ....models.entity import Entity, EntityType, Relationship
from ....utils.normalization import build_entity, build_relationship


def normalize(response: dict, input_value: str) -> tuple[list[Entity], list[Relationship]]:
    entities: List[Entity] = []
    relationships: List[Relationship] = []

    base_entity = build_entity(
        _infer_entity_type(input_value),
        input_value,
        "alienvault_otx",
        "api",
        0.6,
        {"pulse_count": len(response.get("pulse_info", {}).get("pulses", []))},
    )
    entities.append(base_entity)

    for pulse in response.get("pulse_info", {}).get("pulses", []):
        threat_actor = pulse.get("name")
        if threat_actor:
            actor_entity = build_entity(EntityType.threat_actor, threat_actor, "alienvault_otx", "api", 0.5, {})
            entities.append(actor_entity)
            relationships.append(build_relationship(base_entity, actor_entity, "mentioned_in", 0.5, base_entity.sources))

    return entities, relationships


def _infer_entity_type(input_value: str) -> EntityType:
    if ":" in input_value or input_value.count(".") == 3:
        return EntityType.ip
    if "." in input_value:
        return EntityType.domain
    return EntityType.file_hash
