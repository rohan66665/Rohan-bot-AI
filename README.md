# 🤖 RAG Bot AI

A full-stack Retrieval-Augmented Generation (RAG) application that uses document retrieval and Large Language Models (LLMs) to generate context-aware responses.

The project combines a Python/FastAPI backend with a React.js frontend, vector search, and containerized deployment.

---

## 🚀 Overview

RAG Bot AI demonstrates a practical RAG workflow for document-based question answering.

The application retrieves relevant information from available documents and provides the retrieved context to an LLM to generate a relevant response.

### RAG Workflow

Documents
↓
Document Processing
↓
Chunking
↓
Embeddings
↓
Vector Search
↓
Relevant Context
↓
LLM
↓
Generated Response

---

## 🧠 Tech Stack

- Python
- FastAPI
- LLM APIs
- LangChain
- Retrieval-Augmented Generation (RAG)
- FAISS / ChromaDB
- React.js
- Docker
- AWS EC2

---

## ⚙️ Features

- Retrieval-Augmented Generation (RAG) based chatbot
- Document-based question answering
- Vector similarity search using FAISS / ChromaDB
- Context-aware responses using LLMs
- React.js frontend connected with FastAPI backend
- Docker-based application setup
- Backend deployment on AWS EC2

---

## 📁 Project Structure

```text
Rohan-bot-AI/
│
├── app/                 # Backend application
├── data/                # Documents and project data
├── frontend/            # Frontend application
├── rag-frontend/        # RAG frontend components/application
├── scripts/             # Utility and setup scripts
├── tests/               # Test files
│
├── Dockerfile           # Docker image configuration
├── docker-compose.yml   # Multi-service Docker configuration
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignored files
└── README.md            # Project documentation


---

## 👨‍💻 Author

**Rohan Sharma**

GitHub: [@rohan66665](https://github.com/rohan66665)
