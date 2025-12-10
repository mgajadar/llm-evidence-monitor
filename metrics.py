# metrics.py
from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer


class EmbeddingMetrics:
    def __init__(self, modelName: str):
        self.model = SentenceTransformer(modelName)

    def similarity(self, textA: str, textB: str) -> float:
        embs = self.model.encode([textA, textB], normalize_embeddings=True)
        return float(np.dot(embs[0], embs[1]))

    def driftScore(self, baseline: str, current: str) -> float:
        """
        1.0 = no drift (perfect match)
        0.0 = complete semantic change
        """
        return self.similarity(baseline, current)
