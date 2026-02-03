from pydantic import BaseModel


class ApiSherlockConfig(BaseModel):
    base_url: str = "https://github.com/sherlock-project/sherlock"
    endpoint: str = "Local tool; sites from repositories"
    rate_limit: str = "Local"
    website: str = "https://github.com/sherlock-project/sherlock"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
