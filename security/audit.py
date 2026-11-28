import logging
from pathlib import Path
from config import ROOT

LOG_DIR = ROOT / ".logs"
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger("Michelle")
logger.setLevel(logging.INFO)

handler = logging.FileHandler(LOG_DIR / "michelle.log")
handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))

logger.addHandler(handler)

def log_event(event, details):
    logger.info("%s | %s", event, details)
