from __future__ import annotations

import typing as t
from abc import abstractstaticmethod
from dataclasses import dataclass, field


@dataclass
class Column:
    attr: str
    text: str = ""
    render: t.Callable = str

    def __post_init__(self):
        if not self.text:
            self.text = self.attr


@dataclass
class GridConfig:
    prefix: str = ""
    columns: t.Iterable[Column | str] = field(default_factory=list)
    table_cls = ""

    def __post_init__(self):
        if self.prefix:
            self.prefix = f"{self.prefix}-"

        self.columns = list(
            map(lambda col: Column(col) if isinstance(col, str) else col, self.columns)
        )

    @abstractstaticmethod
    def get_records(
        page: int = 1,
        page_size: int = 20,
        sorts=list[tuple[str, str]],
        q: str = "",
    ) -> tuple[t.Iterable[t.Any], int]:
        ...
