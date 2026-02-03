from pydantic import BaseModel


class MetagoofilConfig(BaseModel):
    command: str = "metagoofil"
    args: list[str] = ['-d', '{input}', '-t', 'pdf']
    timeout_s: int = 30
    notes: str = "Tool execution via subprocess; input injected into args."
