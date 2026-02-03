from pydantic import BaseModel


class AbuseIpdbConfig(BaseModel):
    base_url: str = "https://api.abuseipdb.com/api/v2"
    rate_limit_per_minute: int = 60
    opsec_notes: str = "Passive enrichment only."
