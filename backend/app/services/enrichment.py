from __future__ import annotations

from typing import List

from ..adapters.base import AdapterResponse
from ..models.entity import Entity, Relationship
from ..pipelines.fusion import FusionEngine
from .adapter_registry import AdapterRegistry


class EnrichmentService:
    def __init__(self, fusion_engine: FusionEngine) -> None:
        self._fusion_engine = fusion_engine
        self._registry = AdapterRegistry()

    def list_adapters(self) -> list[str]:
        return list(self._registry.list_adapters().keys())

    def list_catalog(self) -> list[dict]:
        return self._registry.list_catalog()

    async def enrich(self, adapter_name: str, input_value: str) -> AdapterResponse:
        adapter = self._registry.get(adapter_name)
        response = await adapter.enrich(input_value)
        await self._fusion_engine.ingest_entities(response.entities)
        self._fusion_engine.ingest_relationships(response.relationships)
        return response

    def get_entities(self) -> List[Entity]:
        return list(self._fusion_engine._entities.values())

    def get_relationships(self) -> List[Relationship]:
        return list(self._fusion_engine._relationships.values())
