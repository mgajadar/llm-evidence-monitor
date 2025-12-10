# monitor.py
import datetime
from typing import List
from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    OPENAI_MODEL_NAME,
    EMBEDDING_MODEL_NAME,
)
from storage import saveResult, loadHistory
from drift import DriftAnalyzer


class LlmMonitor:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.driftAnalyzer = DriftAnalyzer(EMBEDDING_MODEL_NAME)

    def askModel(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=OPENAI_MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return response.choices[0].message.content.strip()

    def retrieveBaseline(self, prompt: str, history: List[dict]) -> List[str]:
        return [r["answer"] for r in history if r["prompt"] == prompt]

    def monitorOnce(self, prompts: List[str]):
        history = loadHistory()

        for prompt in prompts:
            answer = self.askModel(prompt)
            baselineAnswers = self.retrieveBaseline(prompt, history)

            driftInfo = self.driftAnalyzer.computeDrift(baselineAnswers, answer)

            record = {
                "timestamp": datetime.datetime.utcnow().isoformat(),
                "prompt": prompt,
                "answer": answer,
                "drift": driftInfo["drift"],
                "similarity_avg": driftInfo["similarity_avg"],
            }
            saveResult(record)

            print(f"[monitor] {prompt}")
            print(f"  similarity: {record['similarity_avg']}")
            print(f"  drift: {record['drift']}")
            print()
