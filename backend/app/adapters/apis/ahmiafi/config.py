from pydantic import BaseModel


class AhmiafiConfig(BaseModel):
    base_url: str = "https://ahmia.fi"
    endpoint: str = "https://ahmia.fi/search/?q={query}"
    rate_limit: str = "Fair use / No hard limits"
    website: str = "https://ahmia.fi"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
