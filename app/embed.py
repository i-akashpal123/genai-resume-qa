import os 
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.docstore.document import Document
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def create_embeddings(chunks,save_path='vector_store'):
    print("generating embeddings...")
    embedding_model = HuggingFaceBgeEmbeddings(model_name="all-MiniLM-L6-v2")

    documents = [Document(page_content=chunk) for chunk in chunks]
    vectorstore = FAISS.from_documents(documents,embedding_model)

    vectorstore.save_local(save_path)
    print(f"embeddings saved to '{save_path}/'")