from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable, List

from .models import CommandEntry, CommandsDB, DangerLevel
from ..utils.paths import raw_commands_path, commands_db_path


CATEGORY_PATTERN = re.compile(r"^\s*#\s*(?P<name>.+?)\s*$")
COMMAND_PATTERN = re.compile(r"^(?P<command>[^:]+?)\s*:\s*(?P<description>.+?)\s*$")


def iter_lines(path: Path) -> Iterable[str]:
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")


def infer_danger_level(command: str) -> DangerLevel:
    lowered = command.lower()
    if any(token in lowered for token in ("rm", "dd", "shutdown")):
        return DangerLevel.CRITICAL
    return DangerLevel.SAFE


def parse_raw_commands(path: Path | None = None) -> CommandsDB:
    """
    Parse the raw commands text file into a CommandsDB model.

    Parsing rules:
    - Lines beginning with `#` define the current category.
    - Command lines follow the pattern `command : description`.
    - Empty or unrecognized lines are skipped.
    """
    source = path or raw_commands_path()

    current_category = "Uncategorized"
    entries: List[CommandEntry] = []

    for line in iter_lines(source):
        if not line.strip():
            continue

        category_match = CATEGORY_PATTERN.match(line)
        if category_match:
            current_category = category_match.group("name").strip()
            continue

        cmd_match = COMMAND_PATTERN.match(line)
        if cmd_match:
            command = cmd_match.group("command").strip()
            description = cmd_match.group("description").strip()
            danger_level = infer_danger_level(command)
            entries.append(
                CommandEntry(
                    command=command,
                    description=description,
                    category=current_category,
                    danger_level=danger_level,
                )
            )

    return CommandsDB(commands=entries)


def build_commands_database(
    raw_path: Path | None = None, output_path: Path | None = None
) -> tuple[Path, int]:
    """
    Parse the raw commands file and write the JSON database.

    Returns a tuple of (path, unique_command_count).
    """
    db = parse_raw_commands(raw_path)
    target = output_path or commands_db_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8") as f:
        json.dump(db.model_dump(), f, indent=2, ensure_ascii=False)
    unique_commands = {entry.command for entry in db.commands}
    return target, len(unique_commands)

