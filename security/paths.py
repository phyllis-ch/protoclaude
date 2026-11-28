from pathlib import Path
from config import WORKSPACE

def resolve_path(path: str) -> Path:
    target = (WORKSPACE / path).resolve()

    try:
        target.relative_to(WORKSPACE.resolve())

    except ValueError:
        raise PermissionError("Access forbidden")

    return target



if __name__ == "__main__":
    print(resolve_path(input()))
