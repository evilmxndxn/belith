from pydantic import BaseModel


class MaldatabaseConfig(BaseModel):
    base_url: str = "https://maldatabase.com"
    endpoint: str = "https://maldatabase.com"
    rate_limit: str = "Free for researchers"
    website: str = "https://maldatabase.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
