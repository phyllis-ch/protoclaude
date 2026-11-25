import os
from security.paths import resolve_path

def list_files(path: str = '.') -> str:
    """List files and directories in a path"""
    target = resolve_path(path)
    if not target.is_dir():
        return f"Error: {target} is not a directory."

    entries = os.listdir(target)
    return "\n".join(entries)

def read_file(path: str) -> str:
    """Read contents of a file"""
    target = resolve_path(path)
    if not target.is_file():
        return f"Error: {target} is not found."

    with open(target, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path: str, content: str) -> str:
    """Write content to a file"""
    target = resolve_path(path)
    target.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(target, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully written to {target}"

    except Exception as e:
        return f"Error: {e}"
