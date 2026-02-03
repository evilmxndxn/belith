from __future__ import annotations

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiKeyConfig(BaseModel):
    value: str | None = Field(default=None, description="API key value")
    header_name: str | None = None
    query_name: str | None = None


class RateLimitConfig(BaseModel):
    requests_per_minute: int = 60
    burst: int = 10


class OpsecConfig(BaseModel):
    passive_only: bool = True
    dangerous_tools_allowed: bool = False


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="BELITH_", env_file=".env", extra="ignore")

    api_title: str = "BELITH API"
    api_version: str = "0.1.0"
    opsec_mode: str = "passive"

    request_timeout_s: float = 15.0
    user_agent: str = "BELITH/0.1"

    virustotal_key: str | None = None
    shodan_key: str | None = None
    alienvault_key: str | None = None
    greynoise_key: str | None = None
    whoisxml_key: str | None = None
    abuseipdb_key: str | None = None
    phishtank_key: str | None = None

    certstream_ws_url: str = "wss://certstream.calidog.io"
    openphish_feed_url: str = "https://openphish.com/feed.txt"
    urlhaus_base_url: str = "https://urlhaus-api.abuse.ch/v1"


settings = Settings()
