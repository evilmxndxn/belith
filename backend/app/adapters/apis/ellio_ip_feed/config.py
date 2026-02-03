from pydantic import BaseModel


class EllioIpFeedConfig(BaseModel):
    base_url: str = "https://example.com"
    endpoint: str = "https://example.com"
    rate_limit: str = "24-hour delay for free"
    website: str = "Not specified"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
