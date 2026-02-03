from pydantic import BaseModel


class GreyNoiseConfig(BaseModel):
    base_url: str = "https://api.greynoise.io"
    rate_limit_per_minute: int = 30
    opsec_notes: str = "Passive enrichment only."
