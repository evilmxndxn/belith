from pydantic import BaseModel


class CoinpaprikaConfig(BaseModel):
    base_url: str = "https://api.coinpaprika.com"
    endpoint: str = "https://api.coinpaprika.com/v1/tickers"
    rate_limit: str = "Unlimited"
    website: str = "https://api.coinpaprika.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
