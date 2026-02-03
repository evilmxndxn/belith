from pydantic import BaseModel


class CoincapConfig(BaseModel):
    base_url: str = "https://coincap.io"
    endpoint: str = "https://api.coincap.io/v2/assets"
    rate_limit: str = "Unlimited"
    website: str = "https://coincap.io"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
