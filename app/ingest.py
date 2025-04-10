##This file will handle:

#Reading PDF/Docx files

#Chunking the text

#Saving chunks for embedding

import os 
from PyPDF2 import PdfReader
from docx import Document
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_pdf(file_path:str)-> str:
    reader = PdfReader(file_path)
    return "\n".join([page.extract_text() or "" for page in reader.pages])

def load_txt(file_path:str) ->str:
    with open(file_path,'r',encoding='utf-8') as f:
        return f.read()

def load_docx(file_path:str)->str:
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def load_document(file_path:str)->str:
    if file_path.endswith(".pdf"):
        return load_pdf(file_path) 
    elif file_path.endswith(".txt"):
        return load_txt(file_path)
    elif file_path.endswith(".docx"):
        return load_docx(file_path)
    else:
        raise ValueError("Unsupported file and it has to be in PDF,DOCX,TXT")

def chunk_txt(text:str, chunk_size:int=1000,chunk_overlap:int= 200)-> List[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""]

    )
    return splitter.split_text(text)
    
def process_document(file_path:str)->List[str]:
    print(f"Processing:{file_path}")
    raw_text=load_document(file_path)
    print(f"extracted{len(raw_text)} characters.")
    chunks = chunk_txt(raw_text)
    print(f"split into{len(chunks)} chunks.")
    return chunks 



