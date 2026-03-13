from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
from knowledge_base import DOCUMENTS

embedder = SentenceTransformer("all-MiniLM-L6-v2")

texts = [doc["text"] for doc in DOCUMENTS]
embeddings = embedder.encode(texts)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

faiss.write_index(index, "rag_index.faiss")

with open("rag_docs.pkl", "wb") as f:
    pickle.dump(DOCUMENTS, f)

print("✅ RAG index built successfully")
