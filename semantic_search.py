 
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Load the same embedding model used during ingestion
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def search_clauses(vectorstore, user_query, k=5):
    results = vectorstore.similarity_search(user_query, k=k)
    return results
