from pydantic import BaseModel


class ApicagentConfig(BaseModel):
    base_url: str = "https://apicagent.com"
    endpoint: str = "https://api.apicagent.com/?ua={useragent}"
    rate_limit: str = "Unlimited"
    website: str = "https://apicagent.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
