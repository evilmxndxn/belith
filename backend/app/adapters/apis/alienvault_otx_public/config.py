from pydantic import BaseModel


class AlienvaultOtxPublicConfig(BaseModel):
    base_url: str = "https://otx.alienvault.com"
    endpoint: str = "https://otx.alienvault.com/api/v1/pulses/subscribed (limited public)"
    rate_limit: str = "Limited public / No key for basic"
    website: str = "https://otx.alienvault.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
