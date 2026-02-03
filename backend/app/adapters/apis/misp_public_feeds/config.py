from pydantic import BaseModel


class MispPublicFeedsConfig(BaseModel):
    base_url: str = "https://www.misp-project.org"
    endpoint: str = "Public instance feeds (e.g., https://www.circl.lu/doc/misp/feed-osm/)"
    rate_limit: str = "Fair use"
    website: str = "https://www.misp-project.org"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
