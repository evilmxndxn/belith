from pydantic import BaseModel


class CrtshConfig(BaseModel):
    base_url: str = "https://crt.sh"
    endpoint: str = "https://crt.sh/?q=%25.{domain}&output=json"
    rate_limit: str = "Unlimited"
    website: str = "https://crt.sh"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
