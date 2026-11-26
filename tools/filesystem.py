import os
from security.paths import resolve_path

def list_files(path: str = '.') -> str:
    target = resolve_path(path)
    if not target.is_dir():
        return f"Error: {target} is not a directory."

    entries = os.listdir(target)
    return "\n".join(entries)

def read_file(path: str) -> str:
    target = resolve_path(path)
    if not target.is_file():
        return f"Error: {target} is not found."

    with open(target, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path: str, content: str) -> str:
    target = resolve_path(path)
    target.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(target, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully written to {target}"

    except Exception as e:
        return f"Error: {e}"

def edit_file(path, old_text, new_text):
    target = resolve_path(path)
    if not target.is_file():
        return f"Error: {target} is not found."

    content = target.read_text()
    count = content.count(old_text)
    if count == 0:
        return "Error: Specified text is not found."

    if count > 1:
        return f"Error: Found {count} matches. More context required."

    new_content = content.replace(old_text, new_text, 1)
    target.write_text(new_content)

    return f"Successfully edited {target}"
