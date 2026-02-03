from pydantic import BaseModel


class ShodanConfig(BaseModel):
    base_url: str = "https://api.shodan.io"
    rate_limit_per_minute: int = 30
    opsec_notes: str = "Passive enrichment only."
