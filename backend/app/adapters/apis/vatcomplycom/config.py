from pydantic import BaseModel


class VatcomplycomConfig(BaseModel):
    base_url: str = "https://www.vatcomply.com"
    endpoint: str = "https://api.vatcomply.com/rates"
    rate_limit: str = "Unlimited"
    website: str = "https://www.vatcomply.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
