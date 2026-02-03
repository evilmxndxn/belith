from pydantic import BaseModel


class OpentopodataConfig(BaseModel):
    base_url: str = "https://www.opentopodata.org"
    endpoint: str = "https://api.opentopodata.org/v1/srtm90m?locations={lat}"
    rate_limit: str = "{lon}"
    website: str = "https://www.opentopodata.org"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
