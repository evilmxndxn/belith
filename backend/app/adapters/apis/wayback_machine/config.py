from pydantic import BaseModel


class WaybackMachineConfig(BaseModel):
    base_url: str = "https://web.archive.org"
    endpoint: str = "https://web.archive.org/web/*/{url}"
    rate_limit: str = "Polite usage"
    website: str = "https://web.archive.org"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
