from pydantic import BaseModel


class ThreatfoxConfig(BaseModel):
    base_url: str = "https://threatfox.abuse.ch"
    endpoint: str = "https://threatfox-api.abuse.ch/api/v1/ (POST for queries)"
    rate_limit: str = "Fair use / No key required"
    website: str = "https://threatfox.abuse.ch"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
