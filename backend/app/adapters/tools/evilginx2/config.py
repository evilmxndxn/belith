from pydantic import BaseModel


class Evilginx2Config(BaseModel):
    command: str = "evilginx"
    args: list[str] = ['version']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
