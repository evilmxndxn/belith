from pydantic import BaseModel


class PulsediveCommunityConfig(BaseModel):
    base_url: str = "https://pulsedive.com"
    endpoint: str = "https://pulsedive.com/api/v1/search (community free)"
    rate_limit: str = "Free community tier / Limited"
    website: str = "https://pulsedive.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
