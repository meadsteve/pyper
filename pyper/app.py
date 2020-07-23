from typer import Typer

from pyper.core import wrap_func


class Pyper(Typer):
    def command(self, *args, **kwargs):
        typer_wrapper = super().command(*args, **kwargs)

        def extended_wrapper(func):
            return typer_wrapper(wrap_func(func))

        return extended_wrapper
