from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Sequence

from ..models.entity import Entity, Relationship


@dataclass
class AdapterResponse:
    entities: Sequence[Entity]
    relationships: Sequence[Relationship]
    raw_metadata: dict


class Adapter(Protocol):
    name: str

    async def enrich(self, input_value: str) -> AdapterResponse:
        ...
