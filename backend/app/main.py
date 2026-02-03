from __future__ import annotations

from typing import List

from fastapi import FastAPI, Depends, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from .config.settings import settings
from .config.logging import configure_logging
from .core.auth import verify_token
from .core.file_ingest import ingest_file
from .models.entity import Entity, EntityType, EntitySource, SourceType
from .models.confidence import ConfidenceScore
from .pipelines.fusion import FusionEngine

configure_logging()

app = FastAPI(title=settings.api_title, version=settings.api_version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fusion_engine = FusionEngine()


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


@app.get("/health")
async def health() -> dict:
    return {"status": "ok", "opsec_mode": settings.opsec_mode}
