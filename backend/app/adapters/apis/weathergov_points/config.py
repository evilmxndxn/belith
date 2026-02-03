from pydantic import BaseModel


class WeathergovPointsConfig(BaseModel):
    base_url: str = "https://api.weather.gov"
    endpoint: str = "https://api.weather.gov/points/{lat}"
    rate_limit: str = "{lon}"
    website: str = "https://api.weather.gov"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
