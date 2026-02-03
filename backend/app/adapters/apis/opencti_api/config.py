from pydantic import BaseModel


class OpenctiApiConfig(BaseModel):
    base_url: str = "https://github.com/OpenCTI-Platform/opencti"
    endpoint: str = "API endpoints (e.g., /graphql for queries)"
    rate_limit: str = "Open source / Fair use"
    website: str = "https://github.com/OpenCTI-Platform/opencti"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
