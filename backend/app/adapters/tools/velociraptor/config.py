from pydantic import BaseModel


class VelociraptorConfig(BaseModel):
    command: str = "velociraptor"
    args: list[str] = ['version']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
