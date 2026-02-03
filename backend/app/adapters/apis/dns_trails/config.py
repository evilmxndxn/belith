from pydantic import BaseModel


class DnsTrailsConfig(BaseModel):
    base_url: str = "https://dnstrails.com"
    endpoint: str = "API for IP/domain intel"
    rate_limit: str = "Not specified"
    website: str = "https://dnstrails.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
