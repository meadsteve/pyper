from typing import Iterable

from pyper.core import Prompt, run_generator


def test_with_input(generator, input: Iterable):
    return run_generator(generator, __process_line_faker(input))


def __process_line_faker(fake_input):
    def func(generator, line):
        if isinstance(line, Prompt):
            return generator.send(next(fake_input))
    return func