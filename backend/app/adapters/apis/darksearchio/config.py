from pydantic import BaseModel


class DarksearchioConfig(BaseModel):
    base_url: str = "https://github.com/DarkSearchApp"
    endpoint: str = "Local tool or hosted search"
    rate_limit: str = "Open source / Fair use"
    website: str = "https://github.com/DarkSearchApp"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
