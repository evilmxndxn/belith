from fastapi import Header, HTTPException, status

from ..config.settings import settings


async def verify_token(authorization: str = Header(...)) -> None:
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid auth header")
    token = authorization.split(" ", 1)[1]
    if token != settings.api_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
