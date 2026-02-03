from pydantic import BaseModel


class NormshieldServicesConfig(BaseModel):
    base_url: str = "https://example.com"
    endpoint: str = "https://example.com"
    rate_limit: str = "Free sign up"
    website: str = "Not specified"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
