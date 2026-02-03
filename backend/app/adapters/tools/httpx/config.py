from pydantic import BaseModel


class HttpxConfig(BaseModel):
    command: str = "httpx"
    args: list[str] = ['-u', '{input}']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
