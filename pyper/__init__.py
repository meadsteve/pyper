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


def test_with_input(generator, input: Iterable):
    return __run_generator(generator, __process_line_faker(input))


def _wrap_func(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        generator = func(*args, **kwargs)
        return list(__run_generator(generator))
    return _wrapper


def __process_line(generator, line):
    if isinstance(line, Echo):
        typer.echo(**line.__dict__)
    elif isinstance(line, Prompt):
        user_input = typer.prompt(line.message)
        resp = generator.send(user_input)
        return __process_line(generator, resp)


def __process_line_faker(fake_input):
    def func(generator, line):
        if isinstance(line, Prompt):
            return generator.send(next(fake_input))
    return func


def __run_generator(generator, line_processor=__process_line):
    try:
        while True:
            line = next(generator)
            yield line
            extra_output = line_processor(generator, line)
            if extra_output is not None:
                yield extra_output
    except StopIteration:
        pass
