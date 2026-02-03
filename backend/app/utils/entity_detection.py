from __future__ import annotations

import re

from ..models.entity import EntityType

IP_RE = re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}$")
DOMAIN_RE = re.compile(r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$")
HASH_RE = re.compile(r"^[A-Fa-f0-9]{32,64}$")
URL_RE = re.compile(r"^https?://")
EMAIL_RE = re.compile(r"^[^@]+@[^@]+\.[^@]+$")


def detect_entity_type(value: str, hint: str | None = None) -> EntityType:
    if hint:
        hint_lower = hint.lower()
        if "hash" in hint_lower:
            return EntityType.file_hash
        if "ip" in hint_lower:
            return EntityType.ip
        if "domain" in hint_lower:
            return EntityType.domain
        if "url" in hint_lower:
            return EntityType.url
        if "email" in hint_lower:
            return EntityType.email

    if URL_RE.match(value):
        return EntityType.url
    if EMAIL_RE.match(value):
        return EntityType.email
    if IP_RE.match(value):
        return EntityType.ip
    if HASH_RE.match(value):
        return EntityType.file_hash
    if DOMAIN_RE.match(value):
        return EntityType.domain
    return EntityType.threat
