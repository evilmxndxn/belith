from pydantic import BaseModel


class OpenHashTabConfig(BaseModel):
    command: str = "OpenHashTab"
    args: list[str] = ['--help']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
