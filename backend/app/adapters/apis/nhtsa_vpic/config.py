from pydantic import BaseModel


class NhtsaVpicConfig(BaseModel):
    base_url: str = "https://www.nhtsa.gov"
    endpoint: str = "https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{vin}?format=json"
    rate_limit: str = "Unlimited"
    website: str = "https://www.nhtsa.gov"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
