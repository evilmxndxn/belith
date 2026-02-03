from pydantic import BaseModel


class ArjunConfig(BaseModel):
    command: str = "arjun"
    args: list[str] = ['-u', '{input}']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
