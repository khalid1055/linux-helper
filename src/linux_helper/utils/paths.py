from __future__ import annotations

from pathlib import Path

from platformdirs import user_data_dir


APP_NAME = "linux-helper"
APP_AUTHOR = "linux-helper"


def package_root() -> Path:
    """
    Return the root directory of the installed `linux_helper` package.

    Works both in a source checkout (src layout) and when installed.
    """
    return Path(__file__).resolve().parent.parent


def assets_dir() -> Path:
    """Return the directory that contains bundled asset files."""
    return package_root() / "assets"


def raw_commands_path() -> Path:
    """Path to the bundled raw commands text file."""
    return assets_dir() / "raw_commands.txt"


def commands_db_path() -> Path:
    """Path to the generated JSON commands database."""
    return assets_dir() / "commands.json"


def user_data_path() -> Path:
    """
    Return a writable per-user data directory for linux-helper.

    Currently unused but available for future extensions (e.g. favorites,
    history, or user-specific overrides).
    """
    return Path(user_data_dir(APP_NAME, APP_AUTHOR))

