from __future__ import annotations

from typing import List

from ....models.entity import Entity, EntityType, Relationship
from ....utils.normalization import build_entity, build_relationship


def normalize(message: dict) -> tuple[list[Entity], list[Relationship]]:
    if message.get("message_type") != "certificate_update":
        return [], []
    data = message.get("data", {})
    all_domains = data.get("leaf_cert", {}).get("all_domains", [])
    serial = data.get("leaf_cert", {}).get("serial_number")

    entities: List[Entity] = []
    relationships: List[Relationship] = []

    if serial:
        cert_entity = build_entity(EntityType.certificate, serial, "certstream", "api", 0.5, {})
        entities.append(cert_entity)
    else:
        cert_entity = None

    for domain in all_domains:
        domain_entity = build_entity(EntityType.domain, domain, "certstream", "api", 0.5, {})
        entities.append(domain_entity)
        if cert_entity:
            relationships.append(build_relationship(cert_entity, domain_entity, "observed_for", 0.5, cert_entity.sources))

    return entities, relationships
