from pydantic import BaseModel


class OpenPhishConfig(BaseModel):
    feed_url: str = "https://openphish.com/feed.txt"
    rate_limit_per_minute: int = 30
    opsec_notes: str = "Passive feed retrieval."
