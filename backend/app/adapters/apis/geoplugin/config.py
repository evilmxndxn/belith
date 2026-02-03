from pydantic import BaseModel


class GeopluginConfig(BaseModel):
    base_url: str = "https://www.geoplugin.net"
    endpoint: str = "http://www.geoplugin.net/json.gp?ip={ip}"
    rate_limit: str = "Polite"
    website: str = "https://www.geoplugin.net"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
