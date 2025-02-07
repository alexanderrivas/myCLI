import typer
from commands import command1, command2

app = typer.Typer()

app.add_typer(command1.app, name="comando1")
app.add_typer(command2.app, name="comando2")

if __name__ == "__main__":
    app()