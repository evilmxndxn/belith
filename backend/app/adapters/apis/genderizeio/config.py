from pydantic import BaseModel


class GenderizeioConfig(BaseModel):
    base_url: str = "https://genderize.io"
    endpoint: str = "https://api.genderize.io/?name={name}"
    rate_limit: str = "Free limited"
    website: str = "https://genderize.io"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
