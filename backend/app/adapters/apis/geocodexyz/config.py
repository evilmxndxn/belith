from pydantic import BaseModel


class GeocodexyzConfig(BaseModel):
    base_url: str = "https://geocode.xyz"
    endpoint: str = "https://geocode.xyz/{query}?json=1"
    rate_limit: str = "1 req/sec free"
    website: str = "https://geocode.xyz"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
