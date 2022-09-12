import importlib.metadata
import typer
from pathlib import Path
from typing import List, Optional, Sequence, Union

from comfig.manager import Comfig

__version__ = importlib.metadata.version("comfig")


def version_callback(value: bool):
    if value:
        typer.echo(f"Comfig version: {__version__}")
        raise typer.Exit()


def get_typer(filename: str) -> typer.Typer:
    app = typer.Typer(add_completion=False)
    comfig = Comfig(filename)

    @app.command()
    def get(field: str):
        return comfig[field]

    @app.command()
    def set(field: str, value: str):
        comfig[field] = value

    @app.command()
    def list():
        typer.echo(comfig)

    @app.callback()
    def main(
        version: bool = typer.Option(None, "--version", callback=version_callback, is_eager=True),
    ):
        ...

    return app
