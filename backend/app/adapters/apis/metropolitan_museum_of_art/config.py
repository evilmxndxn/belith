from pydantic import BaseModel


class MetropolitanMuseumOfArtConfig(BaseModel):
    base_url: str = "https://metmuseum.github.io"
    endpoint: str = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
    rate_limit: str = "Unlimited"
    website: str = "https://metmuseum.github.io"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
