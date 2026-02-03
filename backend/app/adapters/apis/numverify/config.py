from pydantic import BaseModel


class NumverifyConfig(BaseModel):
    base_url: str = "https://numverify.com"
    endpoint: str = "Free tier limited"
    rate_limit: str = "Free tier limited"
    website: str = "https://numverify.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
