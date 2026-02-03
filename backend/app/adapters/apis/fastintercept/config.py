from pydantic import BaseModel


class FastinterceptConfig(BaseModel):
    base_url: str = "https://intercept.cloud"
    endpoint: str = "https://intercept.cloud"
    rate_limit: str = "Not specified"
    website: str = "https://intercept.cloud"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
