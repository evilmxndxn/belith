from pydantic import BaseModel


class NagerdateConfig(BaseModel):
    base_url: str = "https://date.nager.at"
    endpoint: str = "https://date.nager.at/Api/v3/PublicHolidays/{year}/{country}"
    rate_limit: str = "Unlimited"
    website: str = "https://date.nager.at"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
