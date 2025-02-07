"""Module providing access command1 actions."""

import typer

app = typer.Typer()


@app.command()
def executar(parametro1: str, parametro2: int):
    """
    Descrição do comando1.

    :param parametro1: Descrição do parametro1.
    :param parametro2: Descrição do parametro2.
    """
    # Lógica do comando1
    print(f"comando1 executado com {parametro1} e {parametro2}")
