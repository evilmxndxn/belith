from pydantic import BaseModel


class RandomfoxConfig(BaseModel):
    base_url: str = "https://randomfox.ca"
    endpoint: str = "https://randomfox.ca/floof/"
    rate_limit: str = "Unlimited"
    website: str = "https://randomfox.ca"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
