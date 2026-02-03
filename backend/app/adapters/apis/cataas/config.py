from pydantic import BaseModel


class CataasConfig(BaseModel):
    base_url: str = "https://cataas.com"
    endpoint: str = "https://cataas.com/cat?json=true"
    rate_limit: str = "Unlimited"
    website: str = "https://cataas.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
