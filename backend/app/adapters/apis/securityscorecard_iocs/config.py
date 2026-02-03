from pydantic import BaseModel


class SecurityscorecardIocsConfig(BaseModel):
    base_url: str = "https://example.com"
    endpoint: str = "https://example.com"
    rate_limit: str = "Public access"
    website: str = "Not specified"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
