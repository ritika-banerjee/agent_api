from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from app.core.kb_loader import load_kb

model = None
index = None
answers = None

def lazy_init():
    global model, index, answers

    if model is None or index is None or answers is None:
        kb = load_kb()
        faqs = kb["drinks_menu_faq"]
        questions = [q["question"] for q in faqs]
        answers = [q["answer"] for q in faqs]

        model = SentenceTransformer("sentence-transformers/gtr-t5-base")
        embeddings = model.encode(questions)
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(np.array(embeddings))

def search_faq(query: str):
    lazy_init()
    vec = model.encode([query])
    _, I = index.search(np.array(vec), 1)
    return {
        "answer": answers[I[0][0]]
    }
