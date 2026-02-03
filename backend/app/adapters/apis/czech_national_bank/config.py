from pydantic import BaseModel


class CzechNationalBankConfig(BaseModel):
    base_url: str = "https://www.cnb.cz"
    endpoint: str = "https://api.cnb.cz/cnbapi/exrates/daily"
    rate_limit: str = "Unlimited"
    website: str = "https://www.cnb.cz"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
