from pydantic import BaseModel


class FocseccomConfig(BaseModel):
    base_url: str = "https://focsec.com"
    endpoint: str = "https://focsec.com"
    rate_limit: str = "Not specified"
    website: str = "https://focsec.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
