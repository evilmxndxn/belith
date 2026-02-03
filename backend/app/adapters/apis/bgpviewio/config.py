from pydantic import BaseModel


class BgpviewioConfig(BaseModel):
    base_url: str = "https://bgpview.io"
    endpoint: str = "https://api.bgpview.io/asn/{asn}"
    rate_limit: str = "Fair use"
    website: str = "https://bgpview.io"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
