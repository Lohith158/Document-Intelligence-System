# Document Intelligence System

A locally running document question-answering system that allows users to upload multiple PDF files and interact with their contents through a conversational chat interface. Powered by Google Gemini and a full RAG pipeline using LangChain and ChromaDB.

---

## Features

- Upload multiple PDF documents simultaneously
- Semantic search across all uploaded documents using vector embeddings
- Natural language question answering grounded strictly in document content
- Clean Gradio-based chat interface accessible via browser
- Persistent ChromaDB vector store for efficient retrieval
- Prevents hallucination through strict context-only prompting

---

## Tech Stack

| Component | Technology |
|---|---|
| LLM | Google Gemini 2.5 Flash |
| Embeddings | HuggingFace all-MiniLM-L6-v2 |
| Vector Database | ChromaDB |
| Framework | LangChain |
| PDF Loader | LangChain PyPDFLoader |
| UI | Gradio |
| Backend | Python |

---

## Project Structure

```
DOC_INTELLIGENCE_AGENT/
├── app.py              # Core logic — RAG pipeline, chat function, Gradio UI
├── .env                # API keys (not committed to Git)
├── chroma_db/          # Persistent vector store (auto-generated)
├── .gitignore
└── README.md
```

---

## How It Works

```
User uploads PDFs
→ PDFs loaded and split into 500-token chunks
→ Chunks converted to vectors using HuggingFace embeddings
→ Vectors stored in ChromaDB

User asks a question
→ Question searched against ChromaDB (semantic similarity)
→ Relevant chunks retrieved as context
→ Context + question sent to Gemini API
→ Answer returned to user via Gradio chat
```

---

## Prerequisites

- Python 3.10 or higher
- Google Gemini API key (free tier available at [aistudio.google.com](https://aistudio.google.com))

---

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/your-username/DOC_INTELLIGENCE_AGENT.git
cd DOC_INTELLIGENCE_AGENT
```

**2. Install dependencies**

```bash
pip install google-generativeai langchain-google-genai gradio pypdf
pip install langchain langchain-community langchain-chroma chromadb
pip install langchain-huggingface sentence-transformers python-dotenv
```

**3. Set up your API key**

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

**4. Run the application**

```bash
python app.py
```

**5. Open the UI**

Visit `http://127.0.0.1:7860` in your browser.

---

## Usage

1. Upload one or more PDF files using the file upload component
2. Click **Process Documents** and wait for confirmation
3. Type your question in the chat box
4. The system retrieves relevant content from your documents and answers accordingly

---

## Example Queries

| Query | Expected Behavior |
|---|---|
| "Summarize this document" | Returns a summary based on retrieved chunks |
| "What does the document say about X?" | Searches and answers from relevant sections |
| "List the key points from the PDF" | Extracts main points from document content |

---

## Key Concepts Demonstrated

- Retrieval Augmented Generation (RAG) pipeline from scratch
- PDF ingestion, chunking, and semantic embedding
- Vector similarity search with ChromaDB
- Cloud LLM integration via Google Gemini API
- Multi-document processing and querying
- Gradio UI for AI application deployment

---

## Author

Lohith G
AI/ML Student
