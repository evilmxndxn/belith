from pydantic import BaseModel


class NmapConfig(BaseModel):
    command: str = "nmap"
    args: list[str] = ['{input}']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
