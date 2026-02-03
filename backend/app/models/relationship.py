from __future__ import annotations

from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime

from pydantic import BaseModel, Field

from .confidence import ConfidenceScore
from .entity import EntitySource


class RelationshipType(str, Enum):
    RESOLVES_TO = "resolves_to"
    ASSOCIATED_WITH = "associated_with"
    SAME_PERSON_AS = "same_person_as"
    OBSERVED_IN = "observed_in"
    DERIVED_FROM = "derived_from"


class Relationship(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    from_entity_id: UUID
    to_entity_id: UUID
    relationship_type: RelationshipType
    source: EntitySource
    confidence: ConfidenceScore = Field(default_factory=lambda: ConfidenceScore(value=0.5))
    timestamp: datetime = Field(default_factory=datetime.utcnow)
