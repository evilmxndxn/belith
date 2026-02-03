from pydantic import BaseModel


class HoneydbConfig(BaseModel):
    base_url: str = "https://honeydb.io"
    endpoint: str = "API for honeypot data"
    rate_limit: str = "Not specified"
    website: str = "https://honeydb.io"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
