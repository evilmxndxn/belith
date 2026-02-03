from pydantic import BaseModel


class SecEdgarConfig(BaseModel):
    base_url: str = "https://www.sec.gov/edgar"
    endpoint: str = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik_padded}.json"
    rate_limit: str = "Unlimited"
    website: str = "https://www.sec.gov/edgar"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
