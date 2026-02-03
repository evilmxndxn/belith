from pydantic import BaseModel


class HydraConfig(BaseModel):
    command: str = "hydra"
    args: list[str] = ['-l', '{input}']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
