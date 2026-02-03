from __future__ import annotations

from typing import List

from ....models.entity import Entity, EntityType, Relationship
from ....utils.normalization import build_entity, build_relationship


def normalize(response: dict, domain: str) -> tuple[list[Entity], list[Relationship]]:
    whois = response.get("WhoisRecord", {})
    registrant = whois.get("registrant", {}) or {}
    registrar = whois.get("registrarName")
    registrant_name = registrant.get("name") or registrant.get("organization")
    registrant_email = registrant.get("email")

    entities: List[Entity] = []
    relationships: List[Relationship] = []

    domain_entity = build_entity(
        EntityType.domain,
        domain,
        "whoisxml",
        "api",
        0.7,
        {
            "created_date": whois.get("createdDate"),
            "updated_date": whois.get("updatedDate"),
            "expires_date": whois.get("expiresDate"),
            "registrar": registrar,
        },
    )
    entities.append(domain_entity)

    if registrant_name:
        org_entity = build_entity(EntityType.organization, registrant_name, "whoisxml", "api", 0.6, {})
        entities.append(org_entity)
        relationships.append(build_relationship(domain_entity, org_entity, "registered_to", 0.6, domain_entity.sources))

    if registrant_email:
        email_entity = build_entity(EntityType.email, registrant_email, "whoisxml", "api", 0.6, {})
        entities.append(email_entity)
        relationships.append(build_relationship(domain_entity, email_entity, "contact_email", 0.5, domain_entity.sources))

    if registrar:
        registrar_entity = build_entity(EntityType.organization, registrar, "whoisxml", "api", 0.5, {})
        entities.append(registrar_entity)
        relationships.append(build_relationship(domain_entity, registrar_entity, "registered_via", 0.4, domain_entity.sources))

    return entities, relationships
