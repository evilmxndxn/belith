from pydantic import BaseModel


class UrlHausConfig(BaseModel):
    base_url: str = "https://urlhaus-api.abuse.ch/v1"
    rate_limit_per_minute: int = 60
    opsec_notes: str = "Passive enrichment only."
