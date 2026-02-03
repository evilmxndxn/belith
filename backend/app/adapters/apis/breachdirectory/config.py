from pydantic import BaseModel


class BreachdirectoryConfig(BaseModel):
    base_url: str = "https://breachdirectory.org"
    endpoint: str = "https://api.breachdirectory.org/?func=auto&term={email}"
    rate_limit: str = "Limited free"
    website: str = "https://breachdirectory.org"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
