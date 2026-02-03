from __future__ import annotations

from typing import List

from fastapi import Depends, FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from .config.logging import configure_logging
from .config.settings import settings
from .core.auth import verify_token
from .core.file_ingest import ingest_file
from .models.entity import Entity, Relationship
from .pipelines.fusion import FusionEngine
from .services.enrichment import EnrichmentService

configure_logging()

app = FastAPI(title=settings.api_title, version=settings.api_version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fusion_engine = FusionEngine()
enrichment_service = EnrichmentService(fusion_engine)


@app.post("/entities/ingest", response_model=List[Entity])
async def ingest_entities(
    entities: List[Entity],
    _: None = Depends(verify_token),
) -> List[Entity]:
    return await fusion_engine.ingest_entities(entities)


@app.post("/files/ingest", response_model=List[Entity])
async def upload_file(
    file: UploadFile = File(...),
    _: None = Depends(verify_token),
) -> List[Entity]:
    from pathlib import Path

    dest_dir = Path("data/uploads")
    entities = await ingest_file(file, dest_dir)
    return await fusion_engine.ingest_entities(entities)


@app.get("/adapters")
async def list_adapters() -> dict:
    return {"adapters": enrichment_service.list_adapters()}


@app.get("/catalog")
async def list_catalog() -> dict:
    return {"items": enrichment_service.list_catalog()}


@app.post("/adapters/{adapter_name}/enrich")
async def enrich(adapter_name: str, input_value: str) -> dict:
    response = await enrichment_service.enrich(adapter_name, input_value)
    return {
        "entities": response.entities,
        "relationships": response.relationships,
        "metadata": response.raw_metadata,
    }


@app.get("/entities", response_model=List[Entity])
async def list_entities() -> List[Entity]:
    return enrichment_service.get_entities()


@app.get("/relationships", response_model=List[Relationship])
async def list_relationships() -> List[Relationship]:
    return enrichment_service.get_relationships()


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "opsec_mode": settings.opsec_mode}
