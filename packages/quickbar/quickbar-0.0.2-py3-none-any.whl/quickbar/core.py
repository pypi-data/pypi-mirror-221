import rich
from typing import Any, List, Literal, Union, Sequence, Iterable, Generator, Tuple
from copy import copy, deepcopy
from rich.console import Console
from rich.progress import (
    Progress, BarColumn, MofNCompleteColumn,
    SpinnerColumn, TextColumn, TimeElapsedColumn,
    TimeRemainingColumn
)

cout = Console()
cerr = Console(stderr=True)

QuickbarKind = Union[Literal["spin"], Literal["step"], Literal["spin-bar"], ]

class Quickbar:
    def __init__(self, kind: QuickbarKind ) -> None:
        self.kind = kind
        self.total = None
        self.task_id = None
        self.is_finite = None
        self.message = "Working .."
        self._spin = Progress(
                SpinnerColumn(),
                "•",
                TextColumn("[bold blue]{task.description}", justify="left"),
                "•",
                TimeElapsedColumn()
            )
        self._spin_bar = Progress(
                SpinnerColumn(),
                "•",
                TextColumn("[bold blue]{task.description}", justify="left"),
                "•",
                BarColumn(),
                "•",
                TimeElapsedColumn(),
                "•",
                TimeRemainingColumn()
            )
        self._step = Progress(
                TextColumn("[bold blue]{task.description}", justify="left"),
                "•",
                BarColumn(),
                "•",
                TimeElapsedColumn(),
                "•",
                TimeRemainingColumn()
            )
        
        if self.kind == 'spin':
            self.bar = self._spin
        elif self.kind ==  'spin-bar':
            self.bar = self._spin_bar
        elif self.kind ==  'step':
            self.bar = self._step
        else:
            self.bar = self._spin_bar
        
    
    @staticmethod
    def track(iterable: Union[Sequence, Iterable] = ..., message: str = 'Working ..'):
        qbar = Quickbar('spin-bar')
        if hasattr(iterable, '__len__'):
            qbar.total = len(iterable)

        
        qbar.message = message or qbar.message
        task_id = qbar.bar.add_task(qbar.message, total=qbar.total)
        def callback():
            qbar.bar.start()
            for item in iterable:
                qbar.bar.advance(task_id=task_id)
                yield item
            qbar.bar.stop()
            qbar.bar.remove_task(task_id=task_id)
        return callback()