from pydantic import BaseModel


class GooglePublicDnsResolverConfig(BaseModel):
    base_url: str = "https://developers.google.com/speed/public-dns"
    endpoint: str = "https://dns.google/resolve?name={domain}&type={type}"
    rate_limit: str = "Very high"
    website: str = "https://developers.google.com/speed/public-dns"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
