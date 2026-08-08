from pathlib import Path
EXCLUDE = { ".venv"}

def tree(path: Path, prefix=""):
    entries = sorted(
        [e for e in path.iterdir() if e.name not in EXCLUDE],
        key=lambda x: (x.is_file(), x.name.lower())
    )

    for i, entry in enumerate(entries):
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + entry.name)

        if entry.is_dir():
            extension = "    " if i == len(entries) - 1 else "│   "
            tree(entry, prefix + extension)

tree(Path("."))