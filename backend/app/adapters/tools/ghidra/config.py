from pydantic import BaseModel


class GhidraConfig(BaseModel):
    command: str = "ghidra"
    args: list[str] = ['--help']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
