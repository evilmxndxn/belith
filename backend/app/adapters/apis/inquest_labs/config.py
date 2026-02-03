from pydantic import BaseModel


class InquestLabsConfig(BaseModel):
    base_url: str = "https://inquest.net"
    endpoint: str = "API for data access"
    rate_limit: str = "Not specified"
    website: str = "https://inquest.net"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
