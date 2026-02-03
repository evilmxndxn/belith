from pydantic import BaseModel


class OsqueryConfig(BaseModel):
    command: str = "osqueryi"
    args: list[str] = ['--help']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
