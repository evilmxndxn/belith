from pydantic import BaseModel


class WiresharkConfig(BaseModel):
    command: str = "tshark"
    args: list[str] = ['-r', '{input}']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
