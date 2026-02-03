from pydantic import BaseModel


class SocialEngineerToolkitConfig(BaseModel):
    command: str = "setoolkit"
    args: list[str] = ['--help']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
