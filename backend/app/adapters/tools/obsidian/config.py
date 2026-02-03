from pydantic import BaseModel


class ObsidianConfig(BaseModel):
    command: str = "obsidian"
    args: list[str] = ['--version']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
