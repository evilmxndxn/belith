from pydantic import BaseModel


class ProwlerConfig(BaseModel):
    command: str = "prowler"
    args: list[str] = ['-h']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
