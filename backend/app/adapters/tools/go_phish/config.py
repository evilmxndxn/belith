from pydantic import BaseModel


class GoPhishConfig(BaseModel):
    command: str = "gophish"
    args: list[str] = ['--help']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
