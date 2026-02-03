from pydantic import BaseModel


class CandcTrackerConfig(BaseModel):
    base_url: str = "https://example.com"
    endpoint: str = "https://example.com"
    rate_limit: str = "Requires license for commercial"
    website: str = "Not specified"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
