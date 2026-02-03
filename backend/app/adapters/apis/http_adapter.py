from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any, Dict

import httpx

from ...config.settings import settings
from ...models.entity import Entity, Relationship
from ...utils.entity_detection import detect_entity_type
from ...utils.normalization import build_entity


@dataclass
class HttpAdapterConfig:
    name: str
    base_url: str
    endpoint: str
    method: str = "GET"
    auth_type: str | None = None
    auth_in: str | None = None
    auth_param: str | None = None
    rate_limit: str | None = None
    website: str | None = None
    notes: str | None = None


class HttpAdapterClient:
    def __init__(self, config: HttpAdapterConfig) -> None:
        self._config = config

    async def request(self, input_value: str) -> dict:
        url = self._build_url(input_value)
        headers: Dict[str, str] = {"User-Agent": settings.user_agent}
        params: Dict[str, str] = {}
        data: Dict[str, str] = {}
        api_key = self._api_key()

        if api_key and self._config.auth_in == "header" and self._config.auth_param:
            headers[self._config.auth_param] = api_key
        if api_key and self._config.auth_in == "query" and self._config.auth_param:
            params[self._config.auth_param] = api_key

        if "{" in url:
            url = url.format(
                query=input_value,
                url=input_value,
                ip=input_value,
                domain=input_value,
                email=input_value,
                hash=input_value,
                asn=input_value,
                cik=input_value,
                indicator=input_value,
                vin=input_value,
                name=input_value,
                country=input_value,
                zip=input_value,
                lat=input_value,
                lon=input_value,
                status_code=input_value,
                status=input_value,
                code=input_value,
                year=input_value,
            )

        if self._config.method.upper() == "POST":
            data = {"query": input_value, "url": input_value, "indicator": input_value}

        async with httpx.AsyncClient(timeout=settings.request_timeout_s) as client:
            response = await client.request(self._config.method, url, params=params, data=data, headers=headers)
            response.raise_for_status()
            return self._parse_response(response)

    def _build_url(self, input_value: str) -> str:
        if self._config.endpoint.startswith("http"):
            return self._config.endpoint
        return f"{self._config.base_url.rstrip('/')}/{self._config.endpoint.lstrip('/')}"

    def _parse_response(self, response: httpx.Response) -> dict:
        content_type = response.headers.get("content-type", "")
        if "json" in content_type:
            return response.json()
        return {"text": response.text}

    def _api_key(self) -> str | None:
        env_key = os.getenv(f"BELITH_{self._config.name.upper()}_KEY")
        if env_key:
            return env_key
        return os.getenv("BELITH_GENERIC_API_KEY")


def normalize_http_response(config: HttpAdapterConfig, input_value: str, payload: dict) -> tuple[list[Entity], list[Relationship]]:
    entity_type = detect_entity_type(input_value)
    entity = build_entity(
        entity_type,
        input_value,
        config.name,
        "api",
        0.5,
        {
            "endpoint": config.endpoint,
            "rate_limit": config.rate_limit,
            "website": config.website,
            "notes": config.notes,
            "response": _safe_summary(payload),
        },
    )
    return [entity], []


def _safe_summary(payload: dict) -> dict:
    try:
        serialized = json.dumps(payload)
    except TypeError:
        return {"summary": str(payload)}
    return {"summary": serialized[:2000]}
