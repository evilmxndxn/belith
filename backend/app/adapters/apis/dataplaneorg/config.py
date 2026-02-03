from pydantic import BaseModel


class DataplaneorgConfig(BaseModel):
    base_url: str = "https://www.dataplane.org"
    endpoint: str = "https://www.dataplane.org"
    rate_limit: str = "No cost"
    website: str = "https://www.dataplane.org"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
