from pydantic import BaseModel


class AlienVaultOtxConfig(BaseModel):
    base_url: str = "https://otx.alienvault.com/api/v1"
    rate_limit_per_minute: int = 20
    opsec_notes: str = "Passive enrichment only."
