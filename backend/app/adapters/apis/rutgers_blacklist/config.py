from pydantic import BaseModel


class RutgersBlacklistConfig(BaseModel):
    base_url: str = "https://example.com"
    endpoint: str = "https://example.com"
    rate_limit: str = "2-hour old"
    website: str = "Not specified"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
