from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Use a free local sentence transformer
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def chunk_and_embed(text):
    # 1. Split into overlapping chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )
    chunks = text_splitter.split_text(text)
    print(f"[INFO] Split into {len(chunks)} chunks.")

    # 2. Create vector store
    vectorstore = FAISS.from_texts(chunks, embeddings)
    print("[INFO] Vector store created.")
    return vectorstore
