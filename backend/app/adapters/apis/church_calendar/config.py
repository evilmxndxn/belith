from pydantic import BaseModel


class ChurchCalendarConfig(BaseModel):
    base_url: str = "https://calapi.inadiutorium.cz"
    endpoint: str = "https://calapi.inadiutorium.cz/api/v2/en/calendar/{date}"
    rate_limit: str = "Unlimited"
    website: str = "https://calapi.inadiutorium.cz"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
