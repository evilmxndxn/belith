from pydantic import BaseModel


class PlacekittenConfig(BaseModel):
    base_url: str = "https://placekitten.com"
    endpoint: str = "https://placekitten.com/{width}/{height}"
    rate_limit: str = "Unlimited"
    website: str = "https://placekitten.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
