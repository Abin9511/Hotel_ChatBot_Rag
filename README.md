 Hotel Chatbot using RAG (FAISS + Gemini AI)

 Project Overview
This project is a **Retrieval-Augmented Generation (RAG)** based hotel chatbot that answers user queries using a hotel knowledge base.

It uses:
- FAISS for fast vector similarity search
- Sentence Transformers for embedding generation
- Google Gemini LLM for response generation
- Flask for web interface

The chatbot follows strict **anti-hallucination rules** and only answers from retrieved knowledge.

---

 Tech Stack
- Python 3.10
- Flask
- FAISS (Vector Database)
- Sentence-Transformers
- Google Gemini API
- HTML/CSS (Frontend)

---

 Architecture

1. User asks a question
2. Query is converted into embeddings
3. FAISS retrieves the closest match from knowledge base
4. If confidence is high → send context to Gemini
5. Gemini generates final response
6. If low confidence → fallback message is shown

---

 Project Structure




---

 How to Run

### 1. Install dependencies

pip install flask faiss-cpu sentence-transformers google-generativeai numpy


