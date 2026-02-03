from pydantic import BaseModel


class CertStreamConfig(BaseModel):
    ws_url: str = "wss://certstream.calidog.io"
    rate_limit_per_minute: int = 60
    opsec_notes: str = "Passive streaming."
