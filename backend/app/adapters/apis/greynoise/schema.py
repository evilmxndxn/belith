from __future__ import annotations

from typing import List

from ....models.entity import Entity, EntityType, Relationship
from ....utils.normalization import build_entity


def normalize(response: dict, ip: str) -> tuple[list[Entity], list[Relationship]]:
    entities: List[Entity] = []
    classification = response.get("classification")
    confidence = 0.7 if classification else 0.5
    ip_entity = build_entity(
        EntityType.ip,
        ip,
        "greynoise",
        "api",
        confidence,
        {
            "noise": response.get("noise"),
            "riot": response.get("riot"),
            "classification": classification,
            "name": response.get("name"),
            "link": response.get("link"),
        },
    )
    entities.append(ip_entity)
    return entities, []
