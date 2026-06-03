import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

with open("knowledge_base.json","r") as rd:
    data = json.load(rd)


text = []

text = [
    item["question"] + " [intent] "+item["question"]
    for item in data
]

embbedding = model.encode(text)

dimension = embbedding.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embbedding))

faiss.write_index(index,"hotel_bot.index")