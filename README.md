# 🧠 AI Memory Router

An AI-powered Memory Router that intelligently routes user queries to the most suitable memory backend before generating a final response using the Groq LLM.

## 🚀 Project Overview

This project demonstrates how an AI Agent can use different memory systems depending on the type of question.

Instead of using Retrieval-Augmented Generation (RAG) for every query, the system classifies the user's request and selects the most appropriate backend.

- 📄 RAG (ChromaDB) → Unstructured document retrieval
- 🕸️ Knowledge Graph → Relationship-based reasoning
- 🗄️ SQLite → Structured data retrieval

Finally, the retrieved context is passed to the Groq LLM to generate an accurate response.

---

## 🏗️ Architecture

```
                User Query
                     │
                     ▼
              Memory Router
                     │
     ┌───────────────┼───────────────┐
     │               │               │
     ▼               ▼               ▼
 ChromaDB      Knowledge Graph     SQLite
   (RAG)          Backend         Database
     │               │               │
     └───────────────┼───────────────┘
                     ▼
              Retrieved Context
                     │
                     ▼
                Groq LLM
                     │
                     ▼
               Final Response
```

---

## ✨ Features

- Intelligent query classification
- Retrieval-Augmented Generation (RAG)
- Knowledge Graph traversal
- SQLite-based structured memory
- Groq LLM integration
- Modular backend architecture
- Easy to extend with new memory systems

---

## 🛠️ Technologies Used

- Python
- Groq API
- ChromaDB
- SQLite
- python-dotenv
- Git & GitHub

---

## 📁 Project Structure

```
agent-memory-router/
│
├── backends/
│   ├── graph.py
│   ├── rag.py
│   └── tabular.py
│
├── router.py
├── main.py
├── .gitignore
├── README.md
└── .env
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/agent-memory-router.git
```

### Navigate into the project

```bash
cd agent-memory-router
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install groq chromadb python-dotenv
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 💻 Example Queries

- What does the refund policy say about electronics?
- How did Project Apollo affect Q3 APAC Revenue?
- What did user 42 order and how much did they spend total?

---

## 📈 Future Improvements

- PDF ingestion
- Neo4j integration
- PostgreSQL backend
- Streamlit UI
- Docker support
- Cloud deployment

---

## 👩‍💻 Author

**Neha Mupparthy**

Final Year B.Tech (Information Technology)

Passionate about AI, Generative AI, LLMs, and Intelligent Agent Systems.
