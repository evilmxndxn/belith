from pydantic import BaseModel


class HoleheConfig(BaseModel):
    command: str = "holehe"
    args: list[str] = ['{input}']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
