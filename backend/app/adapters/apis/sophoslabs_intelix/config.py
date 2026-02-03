from pydantic import BaseModel


class SophoslabsIntelixConfig(BaseModel):
    base_url: str = "https://example.com"
    endpoint: str = "REST APIs"
    rate_limit: str = "Not specified"
    website: str = "Not specified"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
