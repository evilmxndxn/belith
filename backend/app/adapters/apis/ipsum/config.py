from pydantic import BaseModel


class IpsumConfig(BaseModel):
    base_url: str = "https://example.com"
    endpoint: str = "https://example.com"
    rate_limit: str = "Updated daily"
    website: str = "Not specified"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
