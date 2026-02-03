from pydantic import BaseModel


class JamesBrineFeedsConfig(BaseModel):
    base_url: str = "https://example.com"
    endpoint: str = "STIX2 feeds"
    rate_limit: str = "Daily updates"
    website: str = "Not specified"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
