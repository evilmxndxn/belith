from pydantic import BaseModel


class VirusTotalConfig(BaseModel):
    base_url: str = "https://www.virustotal.com/api/v3"
    rate_limit_per_minute: int = 4
    opsec_notes: str = "Passive enrichment only."
