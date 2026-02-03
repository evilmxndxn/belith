from __future__ import annotations

import importlib
import pkgutil
from typing import Dict, List

from ..adapters.base import Adapter


class AdapterRegistry:
    def __init__(self) -> None:
        self._adapters: Dict[str, Adapter] = {}
        self._adapter_types: Dict[str, str] = {}
        self._load_adapters("app.adapters.apis", "api")
        self._load_adapters("app.adapters.tools", "tool")

    def list_adapters(self) -> Dict[str, Adapter]:
        return self._adapters

    def list_catalog(self) -> List[dict]:
        catalog = []
        for name, adapter in sorted(self._adapters.items()):
            catalog.append({"name": name, "type": self._adapter_types.get(name, "api")})
        return catalog

    def get(self, name: str) -> Adapter:
        return self._adapters[name]

    def _load_adapters(self, package_name: str, adapter_type: str) -> None:
        package = importlib.import_module(package_name)
        for module in pkgutil.iter_modules(package.__path__, package.__name__ + "."):
            try:
                imported = importlib.import_module(f"{module.name}.adapter")
            except ModuleNotFoundError:
                continue
            for value in imported.__dict__.values():
                if hasattr(value, "name") and callable(getattr(value, "enrich", None)):
                    try:
                        adapter = value()
                    except Exception:
                        continue
                    self._adapters[adapter.name] = adapter
                    self._adapter_types[adapter.name] = adapter_type
