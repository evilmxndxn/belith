from pydantic import BaseModel


class PhishTankConfig(BaseModel):
    base_url: str = "https://checkurl.phishtank.com/checkurl/"
    rate_limit_per_minute: int = 30
    opsec_notes: str = "Passive URL check."
