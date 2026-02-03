from pydantic import BaseModel


class AgeConfig(BaseModel):
    command: str = "age"
    args: list[str] = ['-h']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
