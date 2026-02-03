from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional


class Settings(BaseSettings):
    api_title: str = "BELITH API"
    api_version: str = "0.1.0"

    # Auth
    api_token: str = Field(default="dev-token", description="Simple bearer token for API access")

    # OPSEC
    opsec_mode: str = Field(default="normal", description="normal|stealth|lab")

    # Example external API keys
    emailrep_api_key: Optional[str] = None
    breachdirectory_api_key: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
