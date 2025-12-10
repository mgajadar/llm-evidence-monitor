# storage.py
import json
from pathlib import Path
from typing import Dict, Any

from config import LOG_FILE, DATA_DIR


def saveResult(record: Dict[str, Any]):
    DATA_DIR.mkdir(exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")


def loadHistory() -> list:
    if not LOG_FILE.exists():
        return []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f.readlines()]
