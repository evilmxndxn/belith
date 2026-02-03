from pydantic import BaseModel


class ShibeonlineConfig(BaseModel):
    base_url: str = "http://shibe.online"
    endpoint: str = "http://shibe.online/api/shibes"
    rate_limit: str = "Unlimited"
    website: str = "http://shibe.online"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
