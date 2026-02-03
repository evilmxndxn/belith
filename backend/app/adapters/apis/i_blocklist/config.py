from pydantic import BaseModel


class IBlocklistConfig(BaseModel):
    base_url: str = "https://www.i-blocklist.com"
    endpoint: str = "https://www.i-blocklist.com"
    rate_limit: str = "Many free"
    website: str = "https://www.i-blocklist.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
