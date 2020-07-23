import pyper

app = pyper.Pyper()


@app.command()
def hello(name: str):
    yield pyper.Echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        yield pyper.Echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        yield pyper.Echo(f"Bye {name}!")


if __name__ == "__main__":
    app()
