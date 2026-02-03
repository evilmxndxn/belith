from pydantic import BaseModel


class HashcatConfig(BaseModel):
    command: str = "hashcat"
    args: list[str] = ['{input}']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
