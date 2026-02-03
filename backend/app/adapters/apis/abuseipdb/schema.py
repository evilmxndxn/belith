from __future__ import annotations

from typing import List

from ....models.entity import Entity, EntityType, Relationship
from ....utils.normalization import build_entity


def normalize(response: dict, ip: str) -> tuple[list[Entity], list[Relationship]]:
    data = response.get("data", {})
    abuse_confidence = data.get("abuseConfidenceScore", 0)
    confidence = min(1.0, 0.4 + abuse_confidence / 100)
    ip_entity = build_entity(
        EntityType.ip,
        ip,
        "abuseipdb",
        "api",
        confidence,
        {
            "abuse_confidence": abuse_confidence,
            "total_reports": data.get("totalReports"),
            "last_reported": data.get("lastReportedAt"),
        },
    )
    return [ip_entity], []
