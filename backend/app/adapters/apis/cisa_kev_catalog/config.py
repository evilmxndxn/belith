from pydantic import BaseModel


class CisaKevCatalogConfig(BaseModel):
    base_url: str = "https://www.cisa.gov/known-exploited-vulnerabilities"
    endpoint: str = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    rate_limit: str = "Unlimited"
    website: str = "https://www.cisa.gov/known-exploited-vulnerabilities"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
