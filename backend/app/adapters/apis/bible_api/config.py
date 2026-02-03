from pydantic import BaseModel


class BibleApiConfig(BaseModel):
    base_url: str = "https://bible-api.com"
    endpoint: str = "https://bible-api.com/john+3:16"
    rate_limit: str = "Unlimited"
    website: str = "https://bible-api.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
