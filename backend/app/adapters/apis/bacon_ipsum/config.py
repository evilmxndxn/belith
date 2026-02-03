from pydantic import BaseModel


class BaconIpsumConfig(BaseModel):
    base_url: str = "https://baconipsum.com"
    endpoint: str = "https://baconipsum.com/api/?type=all-meat"
    rate_limit: str = "Unlimited"
    website: str = "https://baconipsum.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
