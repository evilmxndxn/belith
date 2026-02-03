from pydantic import BaseModel


class IpapiConfig(BaseModel):
    base_url: str = "https://ip-api.com"
    endpoint: str = "http://ip-api.com/json/{ip}"
    rate_limit: str = "45 req/min"
    website: str = "https://ip-api.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
