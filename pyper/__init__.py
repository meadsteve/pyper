import functools
from dataclasses import dataclass
from typing import Any, TypeVar, Iterable

import typer


@dataclass
class Echo:
    message: str
    file: Any = None
    nl: bool = True
    err: bool = False
    color: Any = None


@dataclass
class Prompt:
    message: str


def run(func):
    wrapped_func = _wrap_func(func)
    typer.run(wrapped_func)


def _wrap_func(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        generator = func(*args, **kwargs)
        return list(__run_generator(generator))
    return _wrapper


def test_with_input(generator, input: Iterable):
    try:
        while True:
            line = next(generator)
            yield line
            if isinstance(line, Prompt):
                yield generator.send(next(input))
    except StopIteration:
        pass


def __run_generator(generator):
    try:
        while True:
            line = next(generator)
            yield line
            if isinstance(line, Echo):
                typer.echo(**line.__dict__)
            elif isinstance(line, Prompt):
                resp = typer.prompt(line.message)
                generator.send(resp)
    except StopIteration:
        pass
