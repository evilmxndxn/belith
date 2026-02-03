from pydantic import BaseModel


class UniversitiesHipolabsConfig(BaseModel):
    base_url: str = "http://universities.hipolabs.com"
    endpoint: str = "http://universities.hipolabs.com/search?country={country}"
    rate_limit: str = "Unlimited"
    website: str = "http://universities.hipolabs.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
