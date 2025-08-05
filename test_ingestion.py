from ingestion.pdf_reader import extract_text_from_pdf
from vector_store.embed_store import chunk_and_embed
from semantic_search import search_clauses
from query_parser import parse_query
from decision_engine import evaluate_decision

# Step 1: Extract document
text = extract_text_from_pdf("sample_files/sample.pdf")

# Step 2: Embed and store
vs = chunk_and_embed(text)

# ✅ Define your query before using it
query = "My dad, 52, had a knee surgery in Pune 2 months ago. Can we claim?"

# Step 3: Retrieve relevant policy clauses
results = search_clauses(vs, query)

# Step 4: Parse structured info from query
parsed_query = parse_query(query)

# Step 5: Use AI to evaluate and decide
decision = evaluate_decision(parsed_query, results)

# Step 6: Show results
print("\n--- Final Decision ---")
print(decision)
