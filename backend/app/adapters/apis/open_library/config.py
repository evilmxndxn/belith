from pydantic import BaseModel


class OpenLibraryConfig(BaseModel):
    base_url: str = "https://openlibrary.org/developers/api"
    endpoint: str = "https://openlibrary.org/search.json?q={query}"
    rate_limit: str = "Unlimited"
    website: str = "https://openlibrary.org/developers/api"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
