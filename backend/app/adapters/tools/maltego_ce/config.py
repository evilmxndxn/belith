from pydantic import BaseModel


class MaltegoCeConfig(BaseModel):
    command: str = "maltego"
    args: list[str] = ['--help']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
