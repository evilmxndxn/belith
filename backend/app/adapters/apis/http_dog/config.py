from pydantic import BaseModel


class HttpDogConfig(BaseModel):
    base_url: str = "https://http.dog"
    endpoint: str = "https://http.dog/{status_code}"
    rate_limit: str = "Unlimited"
    website: str = "https://http.dog"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
