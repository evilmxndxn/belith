from pydantic import BaseModel


class RandomduckConfig(BaseModel):
    base_url: str = "https://random-d.uk"
    endpoint: str = "https://random-d.uk/api/v2/random"
    rate_limit: str = "Unlimited"
    website: str = "https://random-d.uk"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
