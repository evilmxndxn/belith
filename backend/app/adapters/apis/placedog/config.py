from pydantic import BaseModel


class PlacedogConfig(BaseModel):
    base_url: str = "https://place.dog"
    endpoint: str = "https://place.dog/{width}/{height}"
    rate_limit: str = "Unlimited"
    website: str = "https://place.dog"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
