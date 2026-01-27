from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class DangerLevel(str, Enum):
    SAFE = "safe"
    CRITICAL = "critical"


class CommandEntry(BaseModel):
    """
    One command entry in the commands database.
    """

    command: str = Field(..., description="The raw shell command, e.g. `ls -la`.")
    description: str = Field(..., description="Human readable description.")
    category: str = Field(..., description="High level category parsed from headers.")
    danger_level: DangerLevel = Field(
        DangerLevel.SAFE,
        description="Heuristic danger level for the command.",
    )


class CommandsDB(BaseModel):
    """
    Root model for the commands database JSON file.
    """

    commands: List[CommandEntry] = Field(default_factory=list)

