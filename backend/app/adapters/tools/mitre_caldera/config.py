from pydantic import BaseModel


class MitreCalderaConfig(BaseModel):
    command: str = "caldera"
    args: list[str] = ['--help']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
