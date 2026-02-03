from pydantic import BaseModel


class NationalizeioConfig(BaseModel):
    base_url: str = "https://nationalize.io"
    endpoint: str = "https://api.nationalize.io/?name={name}"
    rate_limit: str = "Free limited"
    website: str = "https://nationalize.io"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
