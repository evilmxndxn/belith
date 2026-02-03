from pydantic import BaseModel


class AnimechanConfig(BaseModel):
    base_url: str = "https://animechan.xyz"
    endpoint: str = "https://animechan.xyz/api/random"
    rate_limit: str = "Unlimited"
    website: str = "https://animechan.xyz"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
