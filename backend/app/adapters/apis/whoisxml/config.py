from pydantic import BaseModel


class WhoisXmlConfig(BaseModel):
    base_url: str = "https://www.whoisxmlapi.com/whoisserver/WhoisService"
    rate_limit_per_minute: int = 20
    opsec_notes: str = "Passive enrichment only."
