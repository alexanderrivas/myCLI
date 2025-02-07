"""Module providing access command2 actions."""

import typer

app = typer.Typer()


@app.command()
def listar(opcao1: bool = False):
    """
    Descrição do comando2.

    :param opcao1: Descrição da opcao1.
    """
    # Lógica do comando2
    print(f"comando2 executado com opcao1={opcao1}")
