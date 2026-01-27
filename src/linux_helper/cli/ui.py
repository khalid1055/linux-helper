from __future__ import annotations

from typing import Iterable, Tuple

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from ..data.models import CommandEntry


console = Console()


def render_welcome(indexed_count: int, db_present: bool) -> None:
    message = Text("linux-helper (lh)", style="bold cyan")
    body = Text(style="white")
    body.append(
        "\n\nType natural language like "
        "'list files in current directory' and I'll suggest Linux commands.\n\n"
    )

    body.append("Currently indexed: ", style="white")
    body.append(str(indexed_count), style="bold green" if indexed_count else "bold yellow")
    body.append(" commands\n", style="white")
    if not db_present:
        body.append("Tip: run ", style="yellow")
        body.append("lh --refresh", style="bold cyan")
        body.append(" to build the command database.\n", style="yellow")

    body.append(
        "\nUsage:\n"
        "  lh \"your query here\"\n"
        "  lh --refresh  # rebuild command database from raw_commands.txt\n"
    )
    panel = Panel(body, title=message, expand=False, border_style="blue")
    console.print(panel)


def render_results(
    query: str, results: Iterable[Tuple[CommandEntry, float]]
) -> None:
    table = Table(title=f"Matches for: [bold]{query}[/bold]", show_lines=False)
    table.add_column("Command", style="bold green")
    table.add_column("Description", style="white")
    table.add_column("Category", style="cyan")
    table.add_column("Danger", style="bold red")
    table.add_column("Score", justify="right", style="magenta")

    for entry, score in results:
        danger_style = "bold red" if entry.danger_level == "critical" else "green"
        table.add_row(
            entry.command,
            entry.description,
            entry.category,
            f"[{danger_style}]{entry.danger_level}[/]",
            f"{score:.0f}",
        )

    console.print(table)


def render_no_results(query: str) -> None:
    console.print(
        Panel.fit(
            Text(
                f"No matches found for query: {query!r}\n"
                "Try rephrasing or using simpler words.",
                style="yellow",
            ),
            border_style="red",
        )
    )

