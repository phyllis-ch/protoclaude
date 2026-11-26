import os
from dotenv import load_dotenv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")

workspace_path = os.getenv("ACCESSIBLE_WORKSPACE", "workspace")
WORKSPACE = Path(workspace_path)
if not WORKSPACE.is_absolute():
    WORKSPACE = ROOT / WORKSPACE
WORKSPACE = WORKSPACE.resolve()
WORKSPACE.mkdir(parents=True, exist_ok=True)

LLM_CLIENT = os.getenv("LLM_CLIENT")
LLM_MODEL = os.getenv("LLM_MODEL")
