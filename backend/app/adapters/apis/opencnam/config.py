from pydantic import BaseModel


class OpencnamConfig(BaseModel):
    base_url: str = "https://www.opencnam.com"
    endpoint: str = "Limited free calls"
    rate_limit: str = "Limited free"
    website: str = "https://www.opencnam.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
