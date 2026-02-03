from pydantic import BaseModel


class DogFactsConfig(BaseModel):
    base_url: str = "https://kinduff.github.io/dog-api/"
    endpoint: str = "https://kinduff.github.io/dog-api/"
    rate_limit: str = "Unlimited"
    website: str = "https://kinduff.github.io/dog-api/"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
