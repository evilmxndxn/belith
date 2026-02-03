from pydantic import BaseModel


class RipestatConfig(BaseModel):
    base_url: str = "https://stat.ripe.net"
    endpoint: str = "https://stat.ripe.net/data/{resource}/data.json"
    rate_limit: str = "Fair use"
    website: str = "https://stat.ripe.net"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
