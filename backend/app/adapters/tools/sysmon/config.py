from pydantic import BaseModel


class SysmonConfig(BaseModel):
    command: str = "sysmon"
    args: list[str] = ['-h']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
