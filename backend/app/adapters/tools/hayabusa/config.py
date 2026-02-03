from pydantic import BaseModel


class HayabusaConfig(BaseModel):
    command: str = "hayabusa"
    args: list[str] = ['-h']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
