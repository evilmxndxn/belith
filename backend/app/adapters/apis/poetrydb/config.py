from pydantic import BaseModel


class PoetrydbConfig(BaseModel):
    base_url: str = "https://poetrydb.org"
    endpoint: str = "https://poetrydb.org/random"
    rate_limit: str = "Unlimited"
    website: str = "https://poetrydb.org"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
