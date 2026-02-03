from pydantic import BaseModel


class WorldTimeApiConfig(BaseModel):
    base_url: str = "http://worldtimeapi.org"
    endpoint: str = "http://worldtimeapi.org/api/ip"
    rate_limit: str = "Unlimited"
    website: str = "http://worldtimeapi.org"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
