from pydantic import BaseModel


class CountapiConfig(BaseModel):
    base_url: str = "https://countapi.xyz"
    endpoint: str = "https://api.countapi.xyz/hit/{namespace}/{key}"
    rate_limit: str = "Unlimited"
    website: str = "https://countapi.xyz"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
