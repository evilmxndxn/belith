from pydantic import BaseModel


class YetiApiConfig(BaseModel):
    base_url: str = "https://github.com/yeti-platform/yeti"
    endpoint: str = "Web API interface"
    rate_limit: str = "Open source / No limits"
    website: str = "https://github.com/yeti-platform/yeti"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
