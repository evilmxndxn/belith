from __future__ import annotations

from typing import List

from ....models.entity import Entity, EntityType, Relationship
from ....utils.normalization import build_entity, build_relationship


def normalize(response: dict, input_value: str) -> tuple[list[Entity], list[Relationship]]:
    data = response.get("data", {})
    attributes = data.get("attributes", {})
    entities: List[Entity] = []
    relationships: List[Relationship] = []

    base_entity_type = _infer_entity_type(data.get("type"), input_value)
    base_entity = build_entity(
        base_entity_type,
        input_value,
        source_name="virustotal",
        source_type="api",
        confidence=0.7,
        metadata={
            "reputation": attributes.get("reputation"),
            "last_analysis_stats": attributes.get("last_analysis_stats"),
        },
        reference_url=attributes.get("links", {}).get("self"),
    )
    entities.append(base_entity)

    malware_names = attributes.get("popular_threat_name") or attributes.get("meaningful_name")
    if malware_names:
        if isinstance(malware_names, str):
            malware_names = [malware_names]
        for name in malware_names:
            malware_entity = build_entity(
                EntityType.malware,
                str(name),
                source_name="virustotal",
                source_type="api",
                confidence=0.6,
                metadata={},
            )
            entities.append(malware_entity)
            relationships.append(
                build_relationship(
                    base_entity,
                    malware_entity,
                    "detected_as",
                    0.6,
                    base_entity.sources,
                )
            )

    return entities, relationships


def _infer_entity_type(data_type: str | None, input_value: str) -> EntityType:
    if data_type == "domain":
        return EntityType.domain
    if data_type == "ip_address":
        return EntityType.ip
    if data_type == "url":
        return EntityType.url
    if data_type == "file":
        return EntityType.file_hash
    if "://" in input_value:
        return EntityType.url
    return EntityType.file_hash
