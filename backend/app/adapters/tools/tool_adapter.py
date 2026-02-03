from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass
from typing import Dict

from ...models.entity import Entity, Relationship
from ...utils.entity_detection import detect_entity_type
from ...utils.normalization import build_entity
from ...utils.time import utc_now


@dataclass
class ToolConfig:
    name: str
    command: str
    args: list[str]
    timeout_s: int = 30
    notes: str | None = None


class ToolRunner:
    def __init__(self, config: ToolConfig) -> None:
        self._config = config

    def run(self, input_value: str) -> dict:
        executable = shutil.which(self._config.command)
        if not executable:
            return {"error": "executable_not_found", "command": self._config.command}
        cmd = [executable] + [arg.replace("{input}", input_value) for arg in self._config.args]
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self._config.timeout_s,
                check=False,
            )
        except subprocess.TimeoutExpired:
            return {"error": "timeout", "command": self._config.command}
        return {"stdout": result.stdout[:2000], "stderr": result.stderr[:2000], "returncode": result.returncode}


def normalize_tool_output(config: ToolConfig, input_value: str, payload: dict) -> tuple[list[Entity], list[Relationship]]:
    entity_type = detect_entity_type(input_value)
    entity = build_entity(
        entity_type,
        input_value,
        config.name,
        "tool",
        0.4,
        {"command": config.command, "args": config.args, "notes": config.notes, "result": payload},
    )
    return [entity], []
