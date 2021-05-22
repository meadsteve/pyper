from typing import Iterable, Union, List

from pyper.core import Prompt, run_generator


def run_with_input(generator, user_inputs: Union[Iterable[str], List[str], str]):
    if isinstance(user_inputs, str):
        user_inputs = [user_inputs]
    if isinstance(user_inputs, list):
        user_inputs = iter(user_inputs)
    return run_generator(generator, __process_line_faker(user_inputs))


def __process_line_faker(fake_input):
    def func(generator, line):
        if isinstance(line, Prompt):
            return generator.send(next(fake_input))
    return func