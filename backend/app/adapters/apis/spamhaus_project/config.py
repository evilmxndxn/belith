from pydantic import BaseModel


class SpamhausProjectConfig(BaseModel):
    base_url: str = "https://www.spamhaus.org"
    endpoint: str = "https://www.spamhaus.org"
    rate_limit: str = "Not specified"
    website: str = "https://www.spamhaus.org"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
