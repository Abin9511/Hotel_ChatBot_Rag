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



 ## Setup and Execution Instructions

### 1. Clone the repository

git clone https://github.com/Abin9511/Hotel_ChatBot_Rag.git

cd Hotel_ChatBot_Rag

### 2. Install dependencies

pip install flask faiss-cpu sentence-transformers google-generativeai numpy

### 3. Configure Gemini API Key

Open gemini.py and add your Gemini API key:

genai.configure(api_key="YOUR_API_KEY")

### 4. Create FAISS Index

Run:

python rag_index.py

(This generates hotel_bot.index from knowledge_base.json)

### 5. Start the application

python main.py

### 6. Open the chatbot

http://127.0.0.1:5000/chatbot

