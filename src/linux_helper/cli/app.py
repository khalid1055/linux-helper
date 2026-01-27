from __future__ import annotations

import sys
from typing import Optional

import click
from rich.console import Console

from ..core.engine import get_indexed_count, search
from ..data.parser import build_commands_database
from .ui import render_no_results, render_results, render_welcome


console = Console()


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option(
    "--refresh",
    "-r",
    is_flag=True,
    help="Rebuild the commands database from raw_commands.txt.",
)
@click.argument("query", nargs=-1)
def main(refresh: bool, query: tuple[str, ...]) -> None:
    """
    linux-helper CLI entry point.

    lh [OPTIONS] [QUERY...]
    """
    joined_query: Optional[str] = " ".join(query).strip() if query else None

    if refresh:
        try:
            _, count = build_commands_database()
            console.print(
                f"[green]Database rebuilt. Total unique commands: [bold]{count}[/bold][/green]"
            )
        except Exception as exc:  # pragma: no cover - defensive
            console.print(f"[red]Failed to rebuild database:[/red] {exc}")
            sys.exit(1)

    if not joined_query:
        count, present = get_indexed_count()
        render_welcome(count, present)
        return

    results = search(joined_query)
    if not results:
        render_no_results(joined_query)
        return

    render_results(joined_query, results)


if __name__ == "__main__":  # pragma: no cover
    main()

