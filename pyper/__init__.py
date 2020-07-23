import typer

from pyper.core import wrap_func
from pyper.core import Echo, Prompt
from pyper.app import Pyper

__all__ = [
    "Echo",
    "Prompt",
    "Pyper"
    "run"
]


def run(func):
    wrapped_func = wrap_func(func)
    typer.run(wrapped_func)


