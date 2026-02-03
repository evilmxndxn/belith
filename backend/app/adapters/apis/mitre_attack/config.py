from pydantic import BaseModel


class MitreAttackConfig(BaseModel):
    stix_url: str = "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"
    rate_limit_per_minute: int = 10
    opsec_notes: str = "Passive data retrieval."
