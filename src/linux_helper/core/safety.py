from __future__ import annotations

from . import __all__  # noqa: F401  # silence potential unused import in linters
from ..data.models import CommandEntry, DangerLevel


DANGEROUS_TOKENS = ("rm", "dd", "shutdown")


def is_potentially_dangerous(command: str) -> bool:
    """
    Heuristic check for potentially dangerous shell commands.
    """
    lowered = command.lower()
    return any(token in lowered for token in DANGEROUS_TOKENS)


def mark_entry_danger(entry: CommandEntry) -> CommandEntry:
    """
    Ensure a `CommandEntry` has an appropriate danger level.
    """
    if is_potentially_dangerous(entry.command):
        entry.danger_level = DangerLevel.CRITICAL
    else:
        entry.danger_level = DangerLevel.SAFE
    return entry

