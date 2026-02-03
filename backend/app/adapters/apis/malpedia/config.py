from pydantic import BaseModel


class MalpediaConfig(BaseModel):
    base_url: str = "https://malpedia.ca"
    endpoint: str = "https://malpedia.ca"
    rate_limit: str = "Not specified"
    website: str = "https://malpedia.ca"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
