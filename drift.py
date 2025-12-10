# drift.py
from typing import List, Dict
from statistics import mean
from metrics import EmbeddingMetrics


class DriftAnalyzer:
    def __init__(self, embedModel: str):
        self.metrics = EmbeddingMetrics(embedModel)

    def computeDrift(self, baselineAnswers: List[str], currentAnswer: str) -> Dict:
        if not baselineAnswers:
            return {
                "similarity_avg": None,
                "drift": None,
                "notes": "baseline empty"
            }

        similarities = [
            self.metrics.driftScore(b, currentAnswer)
            for b in baselineAnswers
        ]
        avg = mean(similarities)
        drift = 1 - avg  # lower avg similarity = more drift

        return {
            "similarity_avg": avg,
            "drift": drift,
            "notes": "higher drift means behavior change"
        }
