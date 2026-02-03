from pydantic import BaseModel


class PlacebearConfig(BaseModel):
    base_url: str = "https://placebear.com"
    endpoint: str = "https://placebear.com/{width}/{height}"
    rate_limit: str = "Unlimited"
    website: str = "https://placebear.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
