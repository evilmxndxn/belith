from pydantic import BaseModel


class PantryConfig(BaseModel):
    base_url: str = "https://getpantry.cloud"
    endpoint: str = "https://getpantry.cloud/pantry/{id}"
    rate_limit: str = "Unlimited"
    website: str = "https://getpantry.cloud"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
