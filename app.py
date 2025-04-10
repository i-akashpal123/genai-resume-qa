from app.ingest import process_document
from app.embed import create_embeddings
from app.search import search
from app.summarize import summarize_text

def run_pipeline(file_path):
    chunks = process_document(file_path)
    create_embeddings(chunks)
    print("🧠 You can now ask questions!")

    while True:
        query = input("Ask a question (or type 'exit'): ")
        if query.lower() == "exit":
            break

        results = search(query)
        combined_text = " ".join(results)

        # 🧠 Try summarizing
        summary = summarize_text(combined_text)

        # Show either summary or fallback
        if summary.startswith("⚠️ Summarization failed"):
            print("\n📌 Top Raw Chunks:")
            for idx, res in enumerate(results, 1):
                print(f"{idx}. {res}\n")
        else:
            print("\n📌 Summarized Answer:")
            print(summary)
        
        print("\n" + "-" * 80)


if __name__ == "__main__":
    file_path = input("📂 Enter path to your document (PDF/TXT/DOCX): ")
    run_pipeline(file_path)
