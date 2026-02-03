from __future__ import annotations

from typing import List, Callable, Awaitable, Dict

from ..models.entity import Entity, EntityType
from ..adapters.apis.whatsmyname.adapter import WhatsMyNameAdapter
from ..adapters.apis.emailrep.adapter import EmailRepAdapter
from ..adapters.apis.ahmia.adapter import AhmiaAdapter
from ..adapters.tools.sherlock.adapter import SherlockAdapter


class TaskEngine:
    def __init__(self) -> None:
        self._api_adapters = {
            "whatsmyname": WhatsMyNameAdapter(),
            "emailrep": EmailRepAdapter(),
            "ahmia": AhmiaAdapter(),
        }
        self._tool_adapters = {
            "sherlock": SherlockAdapter(),
        }

    async def run_for_entities(self, entities: List[Entity]) -> List[Entity]:
        tasks: List[Awaitable[List[Entity]]] = []
        # Simple mapping: usernames -> identity tools; emails -> emailrep; domains/notes -> ahmia
        usernames = [e for e in entities if e.entity_type == EntityType.USERNAME]
        emails = [e for e in entities if e.entity_type == EntityType.EMAIL]
        domains_or_notes = [e for e in entities if e.entity_type in {EntityType.DOMAIN, EntityType.NOTE}]

        if usernames:
            tasks.append(self._api_adapters["whatsmyname"].execute(usernames))  # type: ignore[arg-type]
            tasks.append(self._tool_adapters["sherlock"].execute(usernames))  # type: ignore[arg-type]
        if emails:
            tasks.append(self._api_adapters["emailrep"].execute(emails))  # type: ignore[arg-type]
        if domains_or_notes:
            tasks.append(self._api_adapters["ahmia"].execute(domains_or_notes))  # type: ignore[arg-type]

        results: List[Entity] = []
        if tasks:
            import asyncio

            done = await asyncio.gather(*tasks, return_exceptions=True)
            for r in done:
                if isinstance(r, Exception):
                    continue
                for item in r:
                    if isinstance(item, Entity):
                        results.append(item)
        return results
