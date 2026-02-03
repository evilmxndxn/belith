from pydantic import BaseModel


class CloudflareTraceConfig(BaseModel):
    base_url: str = "https://www.cloudflare.com"
    endpoint: str = "https://www.cloudflare.com/cdn-cgi/trace"
    rate_limit: str = "Unlimited"
    website: str = "https://www.cloudflare.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
