from __future__ import annotations

from fastapi import Header, HTTPException


async def verify_token(authorization: str | None = Header(default=None)) -> None:
    if authorization is None:
        return
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")
