from pydantic import BaseModel


class IntelligenceXConfig(BaseModel):
    base_url: str = "https://intelx.io"
    endpoint: str = "https://intelx.io/api/search (limited free)"
    rate_limit: str = "Free tier limited searches/day"
    website: str = "https://intelx.io"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
