from __future__ import annotations

from typing import List

from ....models.entity import Entity, EntityType, Relationship
from ....utils.normalization import build_entity


def normalize(response: dict, url: str) -> tuple[list[Entity], list[Relationship]]:
    results = response.get("results", {})
    verified = results.get("verified")
    in_database = results.get("in_database")
    confidence = 0.8 if verified else 0.3
    url_entity = build_entity(
        EntityType.url,
        url,
        "phishtank",
        "api",
        confidence,
        {"verified": verified, "in_database": in_database},
    )
    return [url_entity], []
