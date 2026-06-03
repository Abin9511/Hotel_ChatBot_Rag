import json
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

index = faiss.read_index("hotel_bot.index")

with open("knowledge_base.json","r") as r:
    data = json.load(r)

def retrieve(query):

    query_emb = model.encode([query]).astype("float32")

    dist, ind = index.search(query_emb, k=1)

    best_idx = ind[0][0]
    best_dist = dist[0][0]

    print("distance:", best_dist)
    print("best index:", best_idx)

    if best_dist > 35:
        return "Sorry, I don't have that information. Please contact hotel staff."

    return data[best_idx]["answer"]