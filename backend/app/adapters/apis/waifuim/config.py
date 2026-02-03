from pydantic import BaseModel


class WaifuimConfig(BaseModel):
    base_url: str = "https://waifu.im"
    endpoint: str = "https://api.waifu.im/search"
    rate_limit: str = "Unlimited"
    website: str = "https://waifu.im"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
