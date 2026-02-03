from pydantic import BaseModel


class JikanConfig(BaseModel):
    base_url: str = "https://jikan.moe"
    endpoint: str = "https://api.jikan.moe/v4/anime"
    rate_limit: str = "Rate limited"
    website: str = "https://jikan.moe"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
