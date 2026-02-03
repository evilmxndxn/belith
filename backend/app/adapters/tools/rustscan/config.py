from pydantic import BaseModel


class RustscanConfig(BaseModel):
    command: str = "rustscan"
    args: list[str] = ['-a', '{input}']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
