import sh

import pyper
from pyper.testing_helpers import run_with_input


def example_without_input(name: str):
    yield pyper.Echo("Hello")
    yield pyper.Echo(f"I will call you {name}")


def example_with_input(name: str):
    yield pyper.Echo("Hello")
    yield pyper.Echo(f"I will call you {name}")
    resp = yield pyper.Prompt("Are you sure?")
    yield pyper.Echo(f"you said {resp}")


def example_with_many_inputs(name: str):
    yield pyper.Echo("Hello")
    yield pyper.Echo(f"I will call you {name}")
    resp = yield pyper.Prompt("Are you sure?")
    yield pyper.Echo(f"you said {resp}")
    second_resp = yield pyper.Prompt("Are you really sure?")
    yield pyper.Echo(f"you confirmed {second_resp}")


def test_the_example_without_input():
    assert list(example_without_input("steve")) == [
        pyper.Echo("Hello"),
        pyper.Echo(f"I will call you steve")
    ]


def test_the_example_with_input():
    assert list(run_with_input(example_with_input("steve"), "yes")) == [
        pyper.Echo("Hello"),
        pyper.Echo(f"I will call you steve"),
        pyper.Prompt(message='Are you sure?'),
        pyper.Echo(f"you said yes")
    ]


def test_the_example_with_many_inputs():
    assert list(run_with_input(example_with_many_inputs("steve"), ["yes", "of course"])) == [
        pyper.Echo("Hello"),
        pyper.Echo(f"I will call you steve"),
        pyper.Prompt(message='Are you sure?'),
        pyper.Echo(f"you said yes"),
        pyper.Prompt(message='Are you really sure?'),
        pyper.Echo(f"you confirmed of course")
    ]


def test_the_example_dot_py_script_works():
    from io import StringIO
    from os.path import dirname

    output = StringIO()
    sh.python("example.py", "somename", _out=output, _cwd=dirname(__file__) + "/../", _in=("yes",))

    expected = "Hello\nI will call you somename\nAre you sure?: you said yes\n"
    assert output.getvalue() == expected
