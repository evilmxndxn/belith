from pydantic import BaseModel


class QuranConfig(BaseModel):
    base_url: str = "https://api.quran.com"
    endpoint: str = "https://api.quran.com/api/v4/chapters"
    rate_limit: str = "Unlimited"
    website: str = "https://api.quran.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
