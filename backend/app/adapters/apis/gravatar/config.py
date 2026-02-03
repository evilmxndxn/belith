from pydantic import BaseModel


class GravatarConfig(BaseModel):
    base_url: str = "https://gravatar.com"
    endpoint: str = "https://www.gravatar.com/{md5(email)}.json"
    rate_limit: str = "Unlimited"
    website: str = "https://gravatar.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
