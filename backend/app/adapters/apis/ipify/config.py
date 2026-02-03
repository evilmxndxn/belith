from pydantic import BaseModel


class IpifyConfig(BaseModel):
    base_url: str = "https://www.ipify.org"
    endpoint: str = "https://api.ipify.org?format=json"
    rate_limit: str = "Unlimited"
    website: str = "https://www.ipify.org"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
