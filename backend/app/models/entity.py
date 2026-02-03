from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4
from datetime import datetime

from pydantic import BaseModel, Field

from .confidence import ConfidenceScore


class EntityType(str, Enum):
    USERNAME = "username"
    EMAIL = "email"
    PHONE = "phone"
    IP_ADDRESS = "ip_address"
    DOMAIN = "domain"
    GAMER_TAG = "gamer_tag"
    ACCOUNT_ID = "account_id"
    HASH = "hash"
    ALIAS = "alias"
    BEHAVIORAL_EVENT = "behavioral_event"
    NOTE = "note"


class SourceType(str, Enum):
    API = "api"
    TOOL = "tool"
    FILE = "file"


class EntitySource(BaseModel):
    name: str
    type: SourceType


class RelationshipRef(BaseModel):
    relationship_id: UUID
    relationship_type: str


class Entity(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    entity_type: EntityType
    canonical_value: str
    source: EntitySource
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    confidence: ConfidenceScore = Field(default_factory=lambda: ConfidenceScore(value=0.5))
    metadata: Dict[str, Any] = Field(default_factory=dict)
    relationships: List[RelationshipRef] = Field(default_factory=list)
