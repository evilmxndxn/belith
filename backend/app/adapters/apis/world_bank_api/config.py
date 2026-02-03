from pydantic import BaseModel


class WorldBankApiConfig(BaseModel):
    base_url: str = "https://data.worldbank.org"
    endpoint: str = "http://api.worldbank.org/v2/country/{code}/indicator/{indicator}?format=json"
    rate_limit: str = "Unlimited"
    website: str = "https://data.worldbank.org"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
