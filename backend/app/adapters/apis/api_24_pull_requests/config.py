from pydantic import BaseModel


class Api24PullRequestsConfig(BaseModel):
    base_url: str = "https://24pullrequests.com"
    endpoint: str = "API endpoints limited"
    rate_limit: str = "Unlimited"
    website: str = "https://24pullrequests.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
