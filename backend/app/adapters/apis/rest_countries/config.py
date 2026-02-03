from pydantic import BaseModel


class RestCountriesConfig(BaseModel):
    base_url: str = "https://restcountries.com"
    endpoint: str = "https://restcountries.com/v3.1/all"
    rate_limit: str = "Unlimited"
    website: str = "https://restcountries.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
