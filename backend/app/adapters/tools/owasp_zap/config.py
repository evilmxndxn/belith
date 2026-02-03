from pydantic import BaseModel


class OwaspZapConfig(BaseModel):
    command: str = "zap-cli"
    args: list[str] = ['quick-scan', '{input}']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
