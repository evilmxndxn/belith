from pydantic import BaseModel


class BotvrijeuConfig(BaseModel):
    base_url: str = "https://botvrij.eu"
    endpoint: str = "https://botvrij.eu"
    rate_limit: str = "Not specified"
    website: str = "https://botvrij.eu"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
