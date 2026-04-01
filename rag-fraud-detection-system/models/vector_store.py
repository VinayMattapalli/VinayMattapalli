import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from functools import lru_cache


class VectorStore:

    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

        self.texts = [
            "Transactions above $2000 are high risk",
            "Low transactions below $100 are safe",
            "Frequent rapid transactions indicate fraud",
            "Foreign transactions are risky"
            ]

        embeddings = self.model.encode(self.texts)

        self.index = faiss.IndexFlatL2(384)
        self.index.add(np.array(embeddings).astype('float32'))

    # ✅ CACHE FUNCTION (NO self here)
    @lru_cache(maxsize=100)
    def cached_encode(self, text):
        return self.model.encode([text]).astype('float32')

    # ✅ SEARCH FUNCTION (USES CACHE)
    def search(self, query_text):
        query_vec = self.cached_encode(query_text)
        distances, indices = self.index.search(query_vec, k=1)
        return self.texts[indices[0][0]]