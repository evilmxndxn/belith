from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Dict, List

from pydantic import BaseModel, Field


class EntityType(str, Enum):
    file_hash = "file_hash"
    domain = "domain"
    ip = "ip"
    url = "url"
    malware = "malware"
    service = "service"
    port = "port"
    organization = "organization"
    threat_actor = "threat_actor"
    scanner = "scanner"
    benign_service = "benign_service"
    email = "email"
    certificate = "certificate"
    tactic = "tactic"
    technique = "technique"
    threat = "threat"


class EntitySource(BaseModel):
    name: str
    source_type: str
    confidence: float | None = None
    reference_url: str | None = None


class Entity(BaseModel):
    id: str
    type: EntityType
    value: str
    sources: List[EntitySource]
    timestamp: datetime
    confidence: float = Field(ge=0.0, le=1.0)
    metadata: Dict[str, str | int | float | bool | None] = Field(default_factory=dict)


class Relationship(BaseModel):
    id: str
    source_id: str
    target_id: str
    relationship_type: str
    confidence: float = Field(ge=0.0, le=1.0)
    provenance: List[EntitySource]
    metadata: Dict[str, str | int | float | bool | None] = Field(default_factory=dict)
