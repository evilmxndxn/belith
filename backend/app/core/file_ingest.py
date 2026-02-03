from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable, List

from fastapi import UploadFile

from ..models.entity import Entity, EntitySource, EntityType
from ..utils.hashing import stable_id
from ..utils.time import utc_now
from ..utils.entity_detection import detect_entity_type


async def ingest_file(file: UploadFile, dest_dir: Path) -> List[Entity]:
    dest_dir.mkdir(parents=True, exist_ok=True)
    contents = await file.read()
    destination = dest_dir / file.filename
    destination.write_bytes(contents)

    text = contents.decode(errors="ignore")
    entities: List[Entity] = []

    if file.filename.endswith(".json"):
        data = json.loads(text)
        items = data if isinstance(data, list) else [data]
        for item in items:
            entities.extend(_entities_from_item(item))
    elif file.filename.endswith(".csv"):
        reader = csv.DictReader(text.splitlines())
        for row in reader:
            entities.extend(_entities_from_item(row))
    else:
        for line in text.splitlines():
            value = line.strip()
            if value:
                entity_type = detect_entity_type(value)
                entities.append(_build_entity(entity_type, value, source="file"))

    return entities


def _entities_from_item(item: dict) -> List[Entity]:
    entities: List[Entity] = []
    for key, value in item.items():
        if value is None:
            continue
        if isinstance(value, list):
            for entry in value:
                entities.extend(_entities_from_item({key: entry}))
        else:
            value_str = str(value)
            entity_type = detect_entity_type(value_str, hint=key)
            entities.append(_build_entity(entity_type, value_str, source=key))
    return entities


def _build_entity(entity_type: EntityType, value: str, source: str) -> Entity:
    return Entity(
        id=stable_id(entity_type.value, value, source),
        type=entity_type,
        value=value,
        sources=[EntitySource(name=source, source_type="file")],
        timestamp=utc_now(),
        confidence=0.4,
        metadata={"ingest_source": source},
    )
