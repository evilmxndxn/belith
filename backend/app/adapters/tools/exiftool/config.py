from pydantic import BaseModel


class ExiftoolConfig(BaseModel):
    command: str = "exiftool"
    args: list[str] = ['{input}']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
