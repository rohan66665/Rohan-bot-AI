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

~~~text
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
~~~

---

## 🐳 Docker

The project includes Docker configuration for running the application in a containerized environment.

~~~bash
docker-compose up --build
~~~

---

## ☁️ Deployment

The backend has been deployed on an AWS EC2 instance.

The deployment workflow includes:

~~~text
Local Development
      ↓
Git / GitHub
      ↓
AWS EC2
      ↓
Python Environment
      ↓
FastAPI Backend
~~~

The EC2 instance can be accessed through SSH for server management and application deployment.

---

## 🔗 Live Demo

https://rohan-ai-chat.vercel.app

> Note: The frontend is hosted separately from the backend. The backend is hosted on AWS EC2, so the live demo may be unavailable when the backend instance is stopped or requires a restart.

---

## 🧪 Testing

The project includes a `tests/` directory for testing application functionality.

---

## 🎯 Key Concepts Demonstrated

- Python backend development
- FastAPI and REST API concepts
- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Vector similarity search
- Document retrieval
- React.js frontend integration
- Docker containerization
- AWS EC2 deployment

---

## 👨‍💻 Author

**Rohan Sharma**

GitHub: [@rohan66665](https://github.com/rohan66665)
