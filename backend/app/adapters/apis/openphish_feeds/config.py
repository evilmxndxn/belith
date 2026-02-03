from pydantic import BaseModel


class OpenphishFeedsConfig(BaseModel):
    base_url: str = "https://openphish.com"
    endpoint: str = "https://openphish.com"
    rate_limit: str = "Free and commercial"
    website: str = "https://openphish.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
