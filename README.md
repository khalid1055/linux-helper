## linux-helper (`lh`)

`linux-helper` is a small CLI tool that turns **natural language queries** into suggested **Linux commands**, using fuzzy matching over a curated command database.

### Features

- **Fuzzy search** of a curated Linux command list using `rapidfuzz`.
- **Nice terminal UI** with `rich` (tables, panels, colors).
- **Safety tagging** of potentially dangerous commands (`rm`, `dd`, `shutdown` → `critical`).
- **Simple database build step** from a raw text file.

### Installation (editable / local)

From the project root:

```bash
pip install -e .
```

This installs the `lh` entry point.

### Usage

- **Search for commands**

```bash
lh "list files in current directory"
```

- **Rebuild the commands database**

```bash
lh --refresh
```

This parses `src/linux_helper/assets/raw_commands.txt` and regenerates `src/linux_helper/assets/commands.json`.

### Project Layout

- `src/linux_helper/assets/raw_commands.txt` – master command list (source of truth).
- `src/linux_helper/assets/commands.json` – generated JSON database.
- `src/linux_helper/data/parser.py` – parses `raw_commands.txt` into JSON (with danger tagging).
- `src/linux_helper/core/engine.py` – fuzzy search engine around the JSON database.
- `src/linux_helper/cli/app.py` – Click-based CLI entry point.
- `scripts/build_db.py` – convenience script to rebuild `commands.json`.

