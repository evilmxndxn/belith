from pydantic import BaseModel


class JohnTheRipperConfig(BaseModel):
    command: str = "john"
    args: list[str] = ['{input}']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
