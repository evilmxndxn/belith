from typing import Optional
import re


def normalize_email(value: str) -> str:
    return value.strip().lower()


def normalize_domain(value: str) -> str:
    return value.strip().lower().rstrip(".")


def normalize_ip(value: str) -> str:
    return value.strip()


def detect_hash_type(value: str) -> Optional[str]:
    v = value.strip().lower()
    if re.fullmatch(r"[0-9a-f]{32}", v):
        return "md5"
    if re.fullmatch(r"[0-9a-f]{40}", v):
        return "sha1"
    if re.fullmatch(r"[0-9a-f]{64}", v):
        return "sha256"
    return None
