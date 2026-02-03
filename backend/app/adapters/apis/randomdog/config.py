from pydantic import BaseModel


class RandomdogConfig(BaseModel):
    base_url: str = "https://random.dog"
    endpoint: str = "https://random.dog/woof.json"
    rate_limit: str = "Unlimited"
    website: str = "https://random.dog"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
