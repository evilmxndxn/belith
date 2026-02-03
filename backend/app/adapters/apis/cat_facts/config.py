from pydantic import BaseModel


class CatFactsConfig(BaseModel):
    base_url: str = "https://catfact.ninja"
    endpoint: str = "https://catfact.ninja/fact"
    rate_limit: str = "Unlimited"
    website: str = "https://catfact.ninja"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
