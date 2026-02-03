from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List
import asyncio
import shlex

from ...core.opsec import is_active_scanning_allowed
from ...models.entity import Entity, EntitySource, SourceType
from ...models.relationship import Relationship


class BaseToolAdapter(ABC):
    name: str
    requires_active_scanning: bool = False

    @staticmethod
    def source() -> EntitySource:
        return EntitySource(name="unknown_tool", type=SourceType.TOOL)

    async def _run_command(self, cmd: str, timeout: int = 60) -> str:
        if self.requires_active_scanning and not is_active_scanning_allowed():
            raise RuntimeError(f"Active scanning not allowed in current OPSEC mode for {self.name}")
        proc = await asyncio.create_subprocess_exec(
            *shlex.split(cmd),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        try:
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        except asyncio.TimeoutError:
            proc.kill()
            raise
        if proc.returncode != 0:
            # stderr intentionally not logged to avoid leaking sensitive info
            raise RuntimeError(f"Tool {self.name} failed with code {proc.returncode}")
        return stdout.decode(errors="ignore")

    @abstractmethod
    async def execute(self, entities: List[Entity]) -> List[Entity | Relationship]:
        ...
