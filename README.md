# LLM Evidence Monitor

Tracks LLM **drift** by re-running a set of baseline prompts over time and
measuring semantic stability using embedding similarity.

## Features

- Runs prompts on a schedule (manual for now)
- Stores history in JSONL
- Semantic drift scoring
- CLI-driven

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your_key_here"
