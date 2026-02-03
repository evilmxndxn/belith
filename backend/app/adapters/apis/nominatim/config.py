from pydantic import BaseModel


class NominatimConfig(BaseModel):
    base_url: str = "https://nominatim.openstreetmap.org"
    endpoint: str = "https://nominatim.openstreetmap.org/search?format=json&q={query}"
    rate_limit: str = "Polite (1 req/sec)"
    website: str = "https://nominatim.openstreetmap.org"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
