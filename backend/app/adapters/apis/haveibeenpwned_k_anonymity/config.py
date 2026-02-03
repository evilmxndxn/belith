from pydantic import BaseModel


class HaveibeenpwnedKAnonymityConfig(BaseModel):
    base_url: str = "https://haveibeenpwned.com"
    endpoint: str = "https://api.pwnedpasswords.com/range/{first5hash}"
    rate_limit: str = "High limits"
    website: str = "https://haveibeenpwned.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
