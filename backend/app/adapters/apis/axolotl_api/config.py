from pydantic import BaseModel


class AxolotlApiConfig(BaseModel):
    base_url: str = "https://axolotlapi.herokuapp.com"
    endpoint: str = "https://axolotlapi.herokuapp.com/v1/facts"
    rate_limit: str = "Unlimited"
    website: str = "https://axolotlapi.herokuapp.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
