from pydantic import BaseModel


class MaigretConfig(BaseModel):
    command: str = "maigret"
    args: list[str] = ['{input}']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
