from __future__ import annotations

from ....adapters.base import AdapterResponse
from ..tool_adapter import ToolConfig, ToolRunner, normalize_tool_output
from .config import ProwlerConfig


class ProwlerAdapter:
    name = "prowler"

    def __init__(self) -> None:
        cfg = ProwlerConfig()
        self._config = ToolConfig(name=self.name, command=cfg.command, args=cfg.args, timeout_s=cfg.timeout_s, notes=cfg.notes)
        self._runner = ToolRunner(self._config)

    async def enrich(self, input_value: str) -> AdapterResponse:
        payload = self._runner.run(input_value)
        entities, relationships = normalize_tool_output(self._config, input_value, payload)
        return AdapterResponse(entities=entities, relationships=relationships, raw_metadata={"source": self.name})
