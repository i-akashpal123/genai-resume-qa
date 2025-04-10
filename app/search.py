import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceBgeEmbeddings
from dotenv import load_dotenv

# 🔐 Load API key securely from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def load_vectorstore(path="vector_store"):  # 🛠 fixed typo: "vectore_store" → "vector_store"
    embedding_model = HuggingFaceBgeEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local(path, embedding_model, allow_dangerous_deserialization=True)


def search(query, k=3):
    print(f"🔎 Searching: {query}")
    vectorstore = load_vectorstore()
    results = vectorstore.similarity_search(query, k=k)
    return [doc.page_content for doc in results]
