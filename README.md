# 🧠 GenAI Resume Q&A App

This is a GenAI-powered Streamlit app that allows you to upload resumes or documents and **chat** with them using smart Q&A and summarization.

### 🔧 Tech Stack
- **LangChain** – for document chunking & vector store
- **FAISS** – for similarity search
- **HuggingFace Transformers** – for summarization
- **Streamlit** – for the interactive web UI
- **Python** – backend logic

---

### 🚀 Features

✅ Upload PDF / DOCX / TXT files  
✅ Ask questions about the document  
✅ Choose between summarized or raw answers  
✅ Clean, simple UI with About & Footer  
✅ Ready for Streamlit Cloud deployment

---

### 📸 Demo

<img width="1436" alt="Screenshot 2025-04-10 at 6 13 09 p m" src="https://github.com/user-attachments/assets/43eeed86-7c68-4273-a20e-6e1184905983" />
 <!-- Optional: Add screenshot if you take one -->

---

### 💻 Local Setup

```bash
git clone https://github.com/i-akashpal123/genai-resume-qa.git
cd genai-resume-qa
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
