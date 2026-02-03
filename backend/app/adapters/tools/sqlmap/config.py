from pydantic import BaseModel


class SqlmapConfig(BaseModel):
    command: str = "sqlmap"
    args: list[str] = ['-u', '{input}']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
