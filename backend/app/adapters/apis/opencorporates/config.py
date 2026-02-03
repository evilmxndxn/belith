from pydantic import BaseModel


class OpencorporatesConfig(BaseModel):
    base_url: str = "https://opencorporates.com"
    endpoint: str = "https://api.opencorporates.com/v0.4/companies/search?q={query}"
    rate_limit: str = "Limited free"
    website: str = "https://opencorporates.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
