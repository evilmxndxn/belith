from pydantic import BaseModel


class IpapicoConfig(BaseModel):
    base_url: str = "https://ipapi.co"
    endpoint: str = "https://ipapi.co/json/"
    rate_limit: str = "1"
    website: str = "https://ipapi.co"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
