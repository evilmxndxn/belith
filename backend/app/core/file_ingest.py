from __future__ import annotations

from typing import List
import csv
import json
from pathlib import Path

from fastapi import UploadFile

from ..models.entity import Entity, EntityType, EntitySource, SourceType
from ..models.confidence import ConfidenceScore


async def ingest_file(upload: UploadFile, dest_dir: Path) -> List[Entity]:
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_path = dest_dir / upload.filename
    content = await upload.read()
    dest_path.write_bytes(content)

    entities: List[Entity] = []
    suffix = dest_path.suffix.lower()

    if suffix == ".csv":
        text = content.decode(errors="ignore").splitlines()
        reader = csv.DictReader(text)
        for row in reader:
            for key, value in row.items():
                if not value:
                    continue
                # naive heuristic: treat as NOTE
                entities.append(
                    Entity(
                        entity_type=EntityType.NOTE,
                        canonical_value=str(value),
                        source=EntitySource(name="file_upload", type=SourceType.FILE),
                        confidence=ConfidenceScore(value=0.4),
                        metadata={"column": key, "filename": upload.filename},
                    )
                )
    elif suffix == ".json":
        data = json.loads(content.decode(errors="ignore"))
        # store as NOTE entities for now
        entities.append(
            Entity(
                entity_type=EntityType.NOTE,
                canonical_value="json_upload",
                source=EntitySource(name="file_upload", type=SourceType.FILE),
                metadata={"filename": upload.filename, "json": data},
            )
        )
    else:
        # treat as plain text
        text = content.decode(errors="ignore")
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            entities.append(
                Entity(
                    entity_type=EntityType.NOTE,
                    canonical_value=line,
                    source=EntitySource(name="file_upload", type=SourceType.FILE),
                    confidence=ConfidenceScore(value=0.3),
                    metadata={"filename": upload.filename},
                )
            )
    return entities
