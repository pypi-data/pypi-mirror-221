from __future__ import annotations

import typing as t

from sqlglot import exp


if t.TYPE_CHECKING:
    from sqlmesh.core.engine_adapter import EngineAdapter
    from sqlmesh.core._typing import TableName



class DataDiff:
    def __init__(self, adapter: EngineAdapter, source: TableName, target: TableName):
        self._adapter = adapter
        self.source = source
        self.target = target

    def schema(self):
        source_columns = self._adapter.columns(self.source)
        target_columns = self._adapter.columns(self.target)
