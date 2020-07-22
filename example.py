import pyper


def main(name: str):
    yield pyper.Echo("Hello")
    yield pyper.Echo(f"I will call you {name}")
    yield pyper.Echo("Bye")


assert list(main("steve")) == [
    pyper.Echo("Hello"),
    pyper.Echo("I will call you steve"),
    pyper.Echo("Bye"),
]

if __name__ == "__main__":
    pyper.run(main)

