from pydantic import BaseModel


class GutendexConfig(BaseModel):
    base_url: str = "https://gutendex.com"
    endpoint: str = "https://gutendex.com/books"
    rate_limit: str = "Unlimited"
    website: str = "https://gutendex.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
