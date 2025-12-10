# app.py
import argparse
from config import OPENAI_API_KEY, OPENAI_MODEL_NAME
from prompts import DEFAULT_PROMPTS
from monitor import LlmMonitor


def runMonitor():
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is not set.")
    print(f"[app] Using model: {OPENAI_MODEL_NAME}")

    mon = LlmMonitor()
    mon.monitorOnce(DEFAULT_PROMPTS)


def showHistory():
    from storage import loadHistory
    hist = loadHistory()
    for r in hist[-10:]:
        print(r)


def main():
    parser = argparse.ArgumentParser(description="LLM Drift Monitor CLI")
    parser.add_argument(
        "command",
        choices=["monitor", "history"],
        help="monitor = run drift check; history = show last entries"
    )
    args = parser.parse_args()

    if args.command == "monitor":
        runMonitor()
    else:
        showHistory()


if __name__ == "__main__":
    main()
