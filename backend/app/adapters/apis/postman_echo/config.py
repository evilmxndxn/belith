from pydantic import BaseModel


class PostmanEchoConfig(BaseModel):
    base_url: str = "https://postman-echo.com"
    endpoint: str = "https://postman-echo.com/get"
    rate_limit: str = "Unlimited"
    website: str = "https://postman-echo.com"
    notes: str = "Assumption: endpoint inferred from provided metadata when missing."
