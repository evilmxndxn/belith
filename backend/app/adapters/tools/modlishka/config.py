from pydantic import BaseModel


class ModlishkaConfig(BaseModel):
    command: str = "modlishka"
    args: list[str] = ['--help']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
