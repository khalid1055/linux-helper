from __future__ import annotations

import json
from pathlib import Path
from typing import List, Tuple

from rapidfuzz import process, fuzz

from ..data.models import CommandEntry, CommandsDB
from ..utils.paths import commands_db_path


def _load_db(path: Path | None = None) -> CommandsDB:
    db_path = path or commands_db_path()
    if not db_path.is_file():
        raise FileNotFoundError(
            f"Commands database not found at {db_path}. "
            "Run `lh --refresh` (or scripts/build_db.py) to generate it."
        )
    with db_path.open("r", encoding="utf-8") as f:
        raw = json.load(f)
    return CommandsDB.model_validate(raw)


def get_indexed_count(path: Path | None = None) -> tuple[int, bool]:
    """
    Return (count, present) for the commands database.

    - count: number of command entries (0 if missing or unreadable)
    - present: whether the JSON file exists on disk
    """
    db_path = path or commands_db_path()
    if not db_path.is_file():
        return 0, False
    try:
        db = _load_db(db_path)
    except Exception:
        return 0, True
    return len(db.commands), True


def search(query: str, limit: int = 5) -> List[Tuple[CommandEntry, float]]:
    """
    Fuzzy search for commands matching the query.

    Returns a list of (CommandEntry, score) tuples, sorted by score descending.
    """
    db = _load_db()
    if not query.strip():
        return []

    choices = [entry.command for entry in db.commands]
    results = process.extract(
        query,
        choices,
        scorer=fuzz.WRatio,
        limit=limit,
    )

    index_by_command = {entry.command: entry for entry in db.commands}
    output: List[Tuple[CommandEntry, float]] = []
    for command, score, _ in results:
        entry = index_by_command.get(command)
        if entry is not None:
            output.append((entry, float(score)))
    return output

