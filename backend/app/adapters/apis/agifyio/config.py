from pydantic import BaseModel


class AgifyioConfig(BaseModel):
    base_url: str = "https://agify.io"
    endpoint: str = "https://api.agify.io/?name={name}"
    rate_limit: str = "Free limited"
    website: str = "https://agify.io"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
