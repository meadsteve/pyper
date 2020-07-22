import functools
from dataclasses import dataclass
from typing import Any, TypeVar

import typer


@dataclass
class Echo:
    message: str
    file: Any = None
    nl: bool = True
    err: bool = False
    color: Any = None


@dataclass
class Return:
    value: Any


def run(func):
    wrapped_func = _wrap_func(func)
    typer.run(wrapped_func)


def _wrap_func(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        for line in func(*args, **kwargs):
            if isinstance(line, Echo):
                typer.echo(**line.__dict__)
            elif isinstance(line, Return):
                return Return.value
    return _wrapper
