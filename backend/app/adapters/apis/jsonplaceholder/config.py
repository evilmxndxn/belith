from pydantic import BaseModel


class JsonplaceholderConfig(BaseModel):
    base_url: str = "https://jsonplaceholder.typicode.com"
    endpoint: str = "https://jsonplaceholder.typicode.com/posts"
    rate_limit: str = "Unlimited"
    website: str = "https://jsonplaceholder.typicode.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
