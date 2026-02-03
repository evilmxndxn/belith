from pydantic import BaseModel


class GreynoiseCommunityConfig(BaseModel):
    base_url: str = "https://viz.greynoise.io"
    endpoint: str = "https://api.greynoise.io/v3/community/{ip}"
    rate_limit: str = "No key for community / Limited queries"
    website: str = "https://viz.greynoise.io"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
