from pydantic import BaseModel


class ArtInstituteOfChicagoConfig(BaseModel):
    base_url: str = "https://api.artic.edu"
    endpoint: str = "https://api.artic.edu/api/v1/artworks"
    rate_limit: str = "Unlimited"
    website: str = "https://api.artic.edu"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
