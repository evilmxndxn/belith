from pydantic import BaseModel


class PickupstixConfig(BaseModel):
    base_url: str = "https://example.com"
    endpoint: str = "https://example.com"
    rate_limit: str = "Free"
    website: str = "Not specified"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
