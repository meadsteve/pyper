# Pyper 
A pure functional wrapper on top of Typer

## Usage
Usage is almost identical to typer (which is used internally)
except instead of calling `typer.echo` which has a side-effect the
functions should yield `pyper.echo` which is a value object. 
```python
import pyper


def main(name: str):
    yield pyper.Echo(f"Hello")
    yield pyper.Echo(f"I will call you {name}")
    yield pyper.Echo(f"Bye")


if __name__ == "__main__":
    pyper.run(main)
```
## Why?
Having the functions yield makes them much easier to test with little
or no mocking:
```python
assert list(main("steve")) == [
    pyper.Echo("Hello"),
    pyper.Echo("I will call you steve"),
    pyper.Echo("Bye"),
]
```