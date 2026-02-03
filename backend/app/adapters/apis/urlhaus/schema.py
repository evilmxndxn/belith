from __future__ import annotations

from typing import List

from ....models.entity import Entity, EntityType, Relationship
from ....utils.normalization import build_entity, build_relationship


def normalize_url(response: dict, url: str) -> tuple[list[Entity], list[Relationship]]:
    entities: List[Entity] = []
    relationships: List[Relationship] = []

    url_entity = build_entity(EntityType.url, url, "urlhaus", "api", 0.7, {"status": response.get("query_status")})
    entities.append(url_entity)

    for entry in response.get("urls", []) or []:
        malware = entry.get("malware")
        if malware:
            malware_entity = build_entity(EntityType.malware, malware, "urlhaus", "api", 0.6, {})
            entities.append(malware_entity)
            relationships.append(build_relationship(url_entity, malware_entity, "hosts", 0.6, url_entity.sources))

    return entities, relationships


def normalize_host(response: dict, host: str) -> tuple[list[Entity], list[Relationship]]:
    entities: List[Entity] = []
    relationships: List[Relationship] = []

    domain_entity = build_entity(EntityType.domain, host, "urlhaus", "api", 0.6, {"status": response.get("query_status")})
    entities.append(domain_entity)

    for entry in response.get("urls", []) or []:
        url = entry.get("url")
        if url:
            url_entity = build_entity(EntityType.url, url, "urlhaus", "api", 0.5, {})
            entities.append(url_entity)
            relationships.append(build_relationship(domain_entity, url_entity, "hosts", 0.5, domain_entity.sources))

    return entities, relationships
