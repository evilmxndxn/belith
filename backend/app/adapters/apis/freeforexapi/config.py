from pydantic import BaseModel


class FreeforexapiConfig(BaseModel):
    base_url: str = "https://freeforexapi.com"
    endpoint: str = "https://freeforexapi.com/api/live"
    rate_limit: str = "Free limited"
    website: str = "https://freeforexapi.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
