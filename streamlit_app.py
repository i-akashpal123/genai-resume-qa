# streamlit_app.py

import streamlit as st
from app.ingest import process_document
from app.embed import create_embeddings
from app.search import search
from app.summarize import summarize_text

st.set_page_config(page_title="GenAI Doc Assistant", layout="centered")

st.title("📄 GenAI Document Q&A Assistant")
st.caption("Chat with your documents. Upload a file and start asking questions!")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt", "docx"])

if uploaded_file is not None:
    with open(f"temp_input.{uploaded_file.type.split('/')[-1]}", "wb") as f:
        f.write(uploaded_file.read())
    
    doc_path = f"temp_input.{uploaded_file.type.split('/')[-1]}"
    st.success("✅ Document uploaded successfully.")

    with st.spinner("Processing and embedding your document..."):
        chunks = process_document(doc_path)
        create_embeddings(chunks)

    st.success("📚 Document processed! You can now ask questions.")
    
    question = st.text_input("Ask a question:")
    use_summary = st.toggle("Summarize the answer", value=True)

    if question:
        with st.spinner("🔍 Searching for answers..."):
            results = search(question)
            combined_text = " ".join([r for r in results if len(r.split()) > 20])

            if use_summary:
                answer = summarize_text(combined_text)
                st.markdown("### 📌 Summarized Answer:")
                st.write(answer)
            else:
                st.markdown("### 📄 Top Retrieved Chunks:")
                for i, chunk in enumerate(results, 1):
                    st.markdown(f"**{i}.** {chunk}")


# --- Footer ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Built by Akash Pal · Powered by LangChain, HuggingFace& Streamlit"
    "</div>",
    unsafe_allow_html=True
)
