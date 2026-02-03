from pydantic import BaseModel


class QuranCloudConfig(BaseModel):
    base_url: str = "https://alquran.cloud/api"
    endpoint: str = "https://api.alquran.cloud/v1/surah"
    rate_limit: str = "Unlimited"
    website: str = "https://alquran.cloud/api"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
