from pydantic import BaseModel


class DomainsdbinfoConfig(BaseModel):
    base_url: str = "https://domainsdb.info"
    endpoint: str = "https://api.domainsdb.info/v1/domains/search?domain={query}"
    rate_limit: str = "Fair use"
    website: str = "https://domainsdb.info"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
