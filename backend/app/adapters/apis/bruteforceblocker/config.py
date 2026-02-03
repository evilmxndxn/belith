from pydantic import BaseModel


class BruteforceblockerConfig(BaseModel):
    base_url: str = "http://danger.rulez.sk/projects/bruteforceblocker"
    endpoint: str = "http://danger.rulez.sk/projects/bruteforceblocker/blist.php"
    rate_limit: str = "None"
    website: str = "http://danger.rulez.sk/projects/bruteforceblocker"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
