from pydantic import BaseModel


class WhatsMyNameConfig(BaseModel):
    command: str = "whatsmyname"
    args: list[str] = ['--help']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
