from __future__ import annotations

from pathlib import Path

from linux_helper.data.parser import build_commands_database


def main() -> None:
    """
    CLI script to (re)build the commands JSON database from raw_commands.txt.
    """
    path, count = build_commands_database()
    print(f"Database rebuilt. Total unique commands: {count}")


if __name__ == "__main__":
    main()

