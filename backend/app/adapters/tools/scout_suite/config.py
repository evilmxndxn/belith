from pydantic import BaseModel


class ScoutSuiteConfig(BaseModel):
    command: str = "scout"
    args: list[str] = ['--help']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
