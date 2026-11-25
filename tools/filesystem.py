import os
from security.paths import resolve_path

def list_files(path: str = '.') -> str:
    """List files and directories in a path"""
    target = resolve_path(path)

    try:
        entries = os.listdir(target)
        return "\n".join(entries)

    except Exception as e:
        return f"Error: {e}"

def read_file(path: str) -> str:
    """Read contents of a file"""
    target = resolve_path(path)

    try:
        with open(target, "r", encoding="utf-8") as f:
            return f.read()

    except Exception as e:
        return f"Error: {e}"

def write_file(path: str, content: str) -> str:
    """Write content to a file"""
    target = resolve_path(path)

    try:
        with open(target, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully written to {target}"

    except Exception as e:
        return f"Error: {e}"
