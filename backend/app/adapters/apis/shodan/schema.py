from __future__ import annotations

from typing import List

from ....models.entity import Entity, EntityType, Relationship
from ....utils.normalization import build_entity, build_relationship


def normalize_host(response: dict, ip: str) -> tuple[list[Entity], list[Relationship]]:
    entities: List[Entity] = []
    relationships: List[Relationship] = []

    ip_entity = build_entity(
        EntityType.ip,
        ip,
        source_name="shodan",
        source_type="api",
        confidence=0.7,
        metadata={
            "organization": response.get("org"),
            "isp": response.get("isp"),
            "ports": response.get("ports"),
        },
        reference_url=response.get("data", [{}])[0].get("link") if response.get("data") else None,
    )
    entities.append(ip_entity)

    org = response.get("org")
    if org:
        org_entity = build_entity(EntityType.organization, org, "shodan", "api", 0.6, {})
        entities.append(org_entity)
        relationships.append(build_relationship(ip_entity, org_entity, "owned_by", 0.5, ip_entity.sources))

    for port in response.get("ports", []):
        port_entity = build_entity(EntityType.port, str(port), "shodan", "api", 0.5, {})
        entities.append(port_entity)
        relationships.append(build_relationship(ip_entity, port_entity, "exposes", 0.5, ip_entity.sources))

    for service in response.get("data", []):
        service_name = service.get("product") or service.get("_shodan", {}).get("module")
        if service_name:
            service_entity = build_entity(EntityType.service, service_name, "shodan", "api", 0.5, {})
            entities.append(service_entity)
            relationships.append(build_relationship(ip_entity, service_entity, "runs", 0.5, ip_entity.sources))

    return entities, relationships


def normalize_domain(response: dict, domain: str) -> tuple[list[Entity], list[Relationship]]:
    entities: List[Entity] = []
    relationships: List[Relationship] = []

    domain_entity = build_entity(EntityType.domain, domain, "shodan", "api", 0.6, {"subdomains": response.get("subdomains")})
    entities.append(domain_entity)

    for subdomain in response.get("subdomains", []):
        full = f"{subdomain}.{domain}"
        sub_entity = build_entity(EntityType.domain, full, "shodan", "api", 0.5, {})
        entities.append(sub_entity)
        relationships.append(build_relationship(domain_entity, sub_entity, "has_subdomain", 0.5, domain_entity.sources))

    return entities, relationships
