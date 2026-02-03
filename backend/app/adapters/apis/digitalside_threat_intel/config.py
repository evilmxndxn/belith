from pydantic import BaseModel


class DigitalsideThreatIntelConfig(BaseModel):
    base_url: str = "https://example.com"
    endpoint: str = "STIX2, CSV, MISP feeds"
    rate_limit: str = "Not specified"
    website: str = "Not specified"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
