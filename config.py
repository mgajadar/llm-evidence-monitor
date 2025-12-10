# config.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

LOG_FILE = DATA_DIR / "monitor_log.jsonl"
PROMPTS_FILE = DATA_DIR / "prompts.txt"  # baseline prompts your system monitors

# model + api
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL_NAME = "gpt-4o-mini"   # change if needed
EMBEDDING_MODEL_NAME = "BAAI/bge-base-en-v1.5"

# monitoring frequency
BATCH_SIZE = 5  # how many prompts to test each run
TOP_K = 5       # retrieval for similarity-based metrics
