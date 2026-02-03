from pydantic import BaseModel


class PowersploitConfig(BaseModel):
    command: str = "powersploit"
    args: list[str] = ['--help']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
