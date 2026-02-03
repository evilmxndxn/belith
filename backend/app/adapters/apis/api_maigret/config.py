from pydantic import BaseModel


class ApiMaigretConfig(BaseModel):
    base_url: str = "https://github.com/soxoj/maigret"
    endpoint: str = "https://raw.githubusercontent.com/soxoj/maigret/main/maigret/sites.json"
    rate_limit: str = "Unlimited"
    website: str = "https://github.com/soxoj/maigret"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
