from pydantic import BaseModel


class FrankfurterConfig(BaseModel):
    base_url: str = "https://www.frankfurter.app"
    endpoint: str = "https://api.frankfurter.app/latest"
    rate_limit: str = "Unlimited"
    website: str = "https://www.frankfurter.app"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
