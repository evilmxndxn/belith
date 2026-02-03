from pydantic import BaseModel


class FileioConfig(BaseModel):
    base_url: str = "https://www.file.io"
    endpoint: str = "https://file.io (POST)"
    rate_limit: str = "Unlimited limited size"
    website: str = "https://www.file.io"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
