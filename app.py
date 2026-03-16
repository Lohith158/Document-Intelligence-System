import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
import dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter

dotenv.load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key = os.getenv("GEMINI_API_KEY"))

vectorstore = None

def process_documents(uploaded_files):
    all_chunks = [] # Empty list for all chunks
    for file in uploaded_files: 
        documents = PyPDFLoader(file).load()  # Loads the pdfs
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50) # Chunks size
        chunks = splitter.split_documents(documents) # Split the doc into chunks
        all_chunks.extend(chunks) # Add to the list of chunks
    embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2") 
    global vectorstore
    vectorstore = Chroma.from_documents(all_chunks, embeddings_model, persist_directory="./chroma_db")
    return "Documents processed successfully!"

def chat(query, chat_history):
    # Optionally use chat_history for context or logging
    if vectorstore is None:
        return "Please upload a PDF first!"
    search_results = vectorstore.similarity_search(query)
    context = " ".join([doc.page_content for doc in search_results])
    prompt = f"Answer based on the context only:\n\nContext: {context}\n\nQuestion: {query}\n\nChat History: {chat_history}"
    response = llm.invoke(prompt)
    return response.content

import gradio as gr

with gr.Blocks() as app:
    gr.Markdown("# Document Intelligence System")
    
    file_input = gr.File(file_count="multiple", label="Upload PDFs")
    upload_btn = gr.Button("Process Documents")
    status = gr.Textbox(label="Status")
    
    upload_btn.click(process_documents, inputs=file_input, outputs=status)
    
    gr.ChatInterface(chat)

app.launch()
