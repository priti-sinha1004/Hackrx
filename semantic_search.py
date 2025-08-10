def search_clauses(vectorstore, query, top_k=5):
    """
    Search for the most relevant clauses in the vector store.

    Args:
        vectorstore: The FAISS vector store instance.
        query (str): The search query text.
        top_k (int): Number of top similar results to return.

    Returns:
        list: List of retrieved documents with metadata.
    """
    if not query or not isinstance(query, str):
        raise ValueError("Query must be a non-empty string.")

    results = vectorstore.similarity_search(query, k=top_k)
    return results
