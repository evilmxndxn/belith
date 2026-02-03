from pydantic import BaseModel


class OpenMeteoConfig(BaseModel):
    base_url: str = "https://open-meteo.com"
    endpoint: str = "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
    rate_limit: str = "<10"
    website: str = "https://open-meteo.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
