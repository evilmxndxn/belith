from pydantic import BaseModel


class TheHarvesterConfig(BaseModel):
    command: str = "theHarvester"
    args: list[str] = ['-d', '{input}', '-b', 'all']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
