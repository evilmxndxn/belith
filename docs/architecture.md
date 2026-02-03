# BELITH Architecture

## Overview
BELITH is an entity-centric intelligence aggregation and fusion platform. All data is normalized into `Entity` and `Relationship` objects and merged deterministically inside the fusion engine.

## Core Components
- **FastAPI backend** (`backend/app`): exposes ingestion and adapter endpoints.
- **Adapters** (`backend/app/adapters`): one adapter per API, each with `adapter.py`, `client.py`, `schema.py`, and `config.py`.
- **Fusion pipeline** (`backend/app/pipelines/fusion.py`): merges entities and relationships across sources.
- **Frontend** (`frontend/src`): provides a panel for each API with entity and relationship views.

## Data Flow
1. User enters an input (IP, domain, URL, etc.) in the UI.
2. The frontend calls `/adapters/{adapter}/enrich`.
3. Each adapter fetches data and normalizes it into entities and relationships.
4. Fusion merges objects by type/value and updates confidence.
5. The UI renders entity chips and relationship summaries.

## Normalization Rules
- Every adapter uses `build_entity` and `build_relationship` helpers.
- Source metadata records origin, confidence, and reference links.
- Entities include timestamps and provenance for fusion transparency.
