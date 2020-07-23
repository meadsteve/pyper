import functools
from dataclasses import dataclass
from typing import Any

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


def __process_line(generator, line):
    if isinstance(line, Echo):
        typer.echo(**line.__dict__)
    elif isinstance(line, Prompt):
        user_input = typer.prompt(line.message)
        resp = generator.send(user_input)
        return __process_line(generator, resp)


def run_generator(generator, line_processor=__process_line):
    try:
        while True:
            line = next(generator)
            yield line
            extra_output = line_processor(generator, line)
            if extra_output is not None:
                yield extra_output
    except StopIteration:
        pass


def wrap_func(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        generator = func(*args, **kwargs)
        return list(run_generator(generator))
    return _wrapper


