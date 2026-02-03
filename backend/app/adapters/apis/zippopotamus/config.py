from pydantic import BaseModel


class ZippopotamusConfig(BaseModel):
    base_url: str = "https://www.zippopotam.us"
    endpoint: str = "https://api.zippopotam.us/{country}/{zip}"
    rate_limit: str = "Unlimited"
    website: str = "https://www.zippopotam.us"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
