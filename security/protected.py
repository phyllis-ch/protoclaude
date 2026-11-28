from pathlib import Path
from config import ROOT, WORKSPACE

def is_protected(path):
    path = Path(path).resolve()
    workspace = WORKSPACE.resolve()
    root = ROOT.resolve()

    try:
        path.relative_to(workspace)
        return False

    except ValueError:
        pass

    try:
        path.relative_to(root)
        return True

    except ValueError:
        return True
