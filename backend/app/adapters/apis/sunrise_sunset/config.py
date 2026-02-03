from pydantic import BaseModel


class SunriseSunsetConfig(BaseModel):
    base_url: str = "https://api.sunrise-sunset.org"
    endpoint: str = "https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}"
    rate_limit: str = "Unlimited"
    website: str = "https://api.sunrise-sunset.org"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
