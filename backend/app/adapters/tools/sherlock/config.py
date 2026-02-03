from pydantic import BaseModel


class SherlockConfig(BaseModel):
    command: str = "sherlock"
    args: list[str] = ['{input}']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
