from pydantic import BaseModel


class MetadefenderCloudConfig(BaseModel):
    base_url: str = "https://www.metadefender.com"
    endpoint: str = "https://www.metadefender.com"
    rate_limit: str = "Updated daily"
    website: str = "https://www.metadefender.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
