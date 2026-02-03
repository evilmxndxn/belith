from pydantic import BaseModel


class HttpCatConfig(BaseModel):
    base_url: str = "https://http.cat"
    endpoint: str = "https://http.cat/{status_code}"
    rate_limit: str = "Unlimited"
    website: str = "https://http.cat"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
