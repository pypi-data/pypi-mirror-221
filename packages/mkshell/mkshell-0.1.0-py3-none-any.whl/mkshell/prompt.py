import rich
import tomllib as tl
from typing import List, Literal, Union
from rich.console import Console
from quickbar import Quickbar

from .memory import Path, Pkg

__all__ = [
    "WELCOME_TEXT",
    "cout",
    "cerr",
    "loop",
    "Explainer"
]

loop = Quickbar.track

cout = Console()
cerr = Console(stderr=True)

WELCOME_TEXT = """


[yellow]███╗░░░███╗██╗░░██╗  ░██████╗██╗░░██╗███████╗██╗░░░░░██╗░░░░░[/yellow]\n
[blue]████╗░████║██║░██╔╝  ██╔════╝██║░░██║██╔════╝██║░░░░░██║░░░░░[/blue]\n
[green]██╔████╔██║█████═╝░  ╚█████╗░███████║█████╗░░██║░░░░░██║░░░░░[/green]\n
[red]██║╚██╔╝██║██╔═██╗░  ░╚═══██╗██╔══██║██╔══╝░░██║░░░░░██║░░░░░[/red]\n
[magenta]██║░╚═╝░██║██║░╚██╗  ██████╔╝██║░░██║███████╗███████╗███████╗[/magenta]\n
[purple]╚═╝░░░░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝[/purple]\n

[bold magenta]Welcome ![/bold magenta]\n
\n
[green]This is MKShell --- short for make-shell.[/green]\n
\n
This tools allows [yellow]two things:[/yellow]\n
\n
- Write pure shell CLIs with basic capabilities using either\n\n
    [green](1)[/green] YAML markup language to document flags, aliases, code\n
    [red](2)[/red] Declarative python code => Library\n
    [blue](3)[/blue] Interactive shell sessions => CLI\n
    \n
if you have any questions, please leave a comment at [link]https://github.com/arnos-stuff/[/link]\n
"""

Explainer = tl.loads((Pkg / 'explain.toml').read_text())