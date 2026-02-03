from pydantic import BaseModel


class BloodhoundConfig(BaseModel):
    command: str = "bloodhound"
    args: list[str] = ['--help']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
