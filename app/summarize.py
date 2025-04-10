# app/summarize.py

from transformers import pipeline
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Load a better model for structured text like resumes or CVs
summarizer = pipeline(
    "summarization",
    model="pszemraj/long-t5-tglobal-base-16384-book-summary",
    tokenizer="pszemraj/long-t5-tglobal-base-16384-book-summary"
)

def summarize_text(text, max_chunk_words=1000):
    """
    Summarize text. If text is short, summarize directly.
    If it's long, break it into chunks, summarize each, and combine.
    """
    try:
        if len(text.split()) <= max_chunk_words:
            summary = summarizer(text, max_length=180, min_length=40, do_sample=False)
            return summary[0]['summary_text']
        
        chunks = []
        words = text.split()
        for i in range(0, len(words), max_chunk_words):
            chunk = " ".join(words[i:i + max_chunk_words])
            summary = summarizer(chunk, max_length=180, min_length=40, do_sample=False)
            chunks.append(summary[0]['summary_text'])
        return "\n\n".join(chunks)
    
    except Exception as e:
        print(f"⚠️ Summarization failed: {e}")
        return "⚠️ Summarization failed. Showing raw results instead."
