from pydantic import BaseModel


class GhuntConfig(BaseModel):
    command: str = "ghunt"
    args: list[str] = ['email', '{input}']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
