import typer

from .prompt import WELCOME_TEXT, loop, cerr, cout, Explainer
from .memory import defaultMemory

from typing import Optional, Union, Any, List
from pathlib import Path

app = typer.Typer(
    name="mkshell",
    help="A tool to autogenerate pure shell CLI-like scripts easily.",
    epilog=WELCOME_TEXT,
    no_args_is_help=True,
    rich_help_panel='rich',
    rich_markup_mode='rich'
)

@app.command("build", help="Build the CLI tool.")
def callback(
    file: str = typer.Option('mkshell.yml', '-f', '--file', help="A shell script described through YAML markup."),
    name: str = typer.Option('shell-script.sh', '-n', '--name', help="The script files' name. If none, the CLI will echo the file result into the terminal."),
    command: Optional[List[str]] = typer.Option(None, '-C', '--command', help="Command name. Can be repeated, but order matters: the first call to `--command` will eat up all flags and args until the next occurence of the flag.", ),
    flags: Optional[List[str]] = typer.Option(None, '-F', '--flags', help="Flags names. Can be repeated, but order matters: the first call to `--command` will eat up all flags and args until the next occurence of `--command`.", ),
    args: Optional[List[str]] = typer.Option(None, '-A', '--args', help="Argument names. Can be repeated, but order matters: the first call to `--command` will eat up all flags and args until the next occurence of the flag.", ),
    ):
    candidates = Path().cwd().rglob(f"**/{file}")
    candidates = list(candidates)
    
    if len(candidates) > 1:
        choices = []
        typer.echo("Mutliple values found:")
        for i, c in enumerate(candidates):
            typer.echo(f"[{i}] path = {c}")
            choices += [i]
        number = typer.prompt("Please pick a number from above", choices=choices, show_default=True, default=0, value_proc=lambda s: int(s))
        if number >= len(choices):
            typer.echo("This was not one of the options, quitting..")
            typer.Exit(1)
    choice = candidates[number]
    
    
@app.command("syntax", help="Explains the YAML syntax expected")
def explain():
    cout.print(WELCOME_TEXT)
    
    cout.print(Explainer)
    
    
    