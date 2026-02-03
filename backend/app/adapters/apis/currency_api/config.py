from pydantic import BaseModel


class CurrencyApiConfig(BaseModel):
    base_url: str = "https://github.com/fawazahmed0/currency-api"
    endpoint: str = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{currency}.json"
    rate_limit: str = "Unlimited"
    website: str = "https://github.com/fawazahmed0/currency-api"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
