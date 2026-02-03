from __future__ import annotations

from typing import List

from ....models.entity import Entity, EntityType, Relationship
from ....utils.normalization import build_entity


def normalize(feed: list[str], url: str) -> tuple[list[Entity], list[Relationship]]:
    entities: List[Entity] = []
    is_phishing = url in set(feed)
    confidence = 0.8 if is_phishing else 0.2
    url_entity = build_entity(
        EntityType.url,
        url,
        "openphish",
        "api",
        confidence,
        {"listed": is_phishing},
    )
    entities.append(url_entity)
    return entities, []
