from pydantic import BaseModel


class ExchangeratehostConfig(BaseModel):
    base_url: str = "https://exchangerate.host"
    endpoint: str = "https://api.exchangerate.host/latest"
    rate_limit: str = "Unlimited"
    website: str = "https://exchangerate.host"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
