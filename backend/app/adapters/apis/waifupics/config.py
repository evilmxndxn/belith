from pydantic import BaseModel


class WaifupicsConfig(BaseModel):
    base_url: str = "https://waifu.pics"
    endpoint: str = "https://api.waifu.pics/sfw/waifu"
    rate_limit: str = "Unlimited"
    website: str = "https://waifu.pics"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
