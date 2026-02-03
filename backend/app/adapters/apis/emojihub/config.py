from pydantic import BaseModel


class EmojihubConfig(BaseModel):
    base_url: str = "https://github.com/cheatsheet/emojihub"
    endpoint: str = "https://emojihub.yurace.pro/api/all"
    rate_limit: str = "Unlimited"
    website: str = "https://github.com/cheatsheet/emojihub"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
