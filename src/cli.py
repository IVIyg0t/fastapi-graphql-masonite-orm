import os

import typer

app = typer.Typer()


@app.command()
def migrate():
    os.system("masonite-orm migrate")


@app.command()
def refresh(seeder: str):
    if seeder:
        os.system(f"masonite-orm migrate:refresh --seed {seeder}")
    else:
        os.system(f"masonite-orm migrate:refresh")


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


if __name__ == "__main__":
    app()
