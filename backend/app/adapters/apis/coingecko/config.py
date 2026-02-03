from pydantic import BaseModel


class CoingeckoConfig(BaseModel):
    base_url: str = "https://www.coingecko.com"
    endpoint: str = "https://api.coingecko.com/api/v3/coins/markets"
    rate_limit: str = "Rate limited fair use"
    website: str = "https://www.coingecko.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
