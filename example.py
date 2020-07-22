import pyper


def main(name: str):
    yield pyper.Echo("Hello")
    yield pyper.Echo(f"I will call you {name}")
    resp = yield pyper.Prompt("Are you sure?")
    yield pyper.Echo(f"you said {resp}")



if __name__ == "__main__":
    pyper.run(main)

