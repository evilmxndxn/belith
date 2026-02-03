from pydantic import BaseModel


class IconHorseConfig(BaseModel):
    base_url: str = "https://icon.horse"
    endpoint: str = "https://icon.horse/icon/{domain}"
    rate_limit: str = "Unlimited"
    website: str = "https://icon.horse"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
