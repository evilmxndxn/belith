from pydantic import BaseModel


class RandomuserConfig(BaseModel):
    base_url: str = "https://randomuser.me"
    endpoint: str = "https://randomuser.me/api/"
    rate_limit: str = "Unlimited"
    website: str = "https://randomuser.me"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
