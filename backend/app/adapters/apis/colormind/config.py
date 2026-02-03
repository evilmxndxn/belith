from pydantic import BaseModel


class ColormindConfig(BaseModel):
    base_url: str = "http://colormind.io"
    endpoint: str = "http://colormind.io/api/"
    rate_limit: str = "Unlimited"
    website: str = "http://colormind.io"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
