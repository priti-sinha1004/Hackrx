 
import streamlit as st
from ingestion.pdf_reader import extract_text_from_pdf
from vector_store.embed_store import chunk_and_embed
from semantic_search import search_clauses
from query_parser import parse_query
from decision_engine import evaluate_decision
import tempfile

st.set_page_config(page_title="Policy Claim AI", layout="centered")
st.title("🤖 Insurance Claim Decision Assistant")

# --- Upload Section ---
uploaded_file = st.file_uploader("📄 Upload your Insurance Policy PDF", type=["pdf"])

query = st.text_area("💬 Describe the claim (e.g., 'Had knee surgery, 52 years old, Pune')")

if st.button("Submit Query") and uploaded_file and query:
    try:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            temp_path = tmp_file.name

        # Step 1: Extract text
        st.info("Reading and processing PDF...")
        text = extract_text_from_pdf(temp_path)

        # Step 2: Embed into vector store
        vector_store = chunk_and_embed(text)

        # Step 3: Semantic search
        results = search_clauses(vector_store, query)

        st.subheader("🔍 Top Matching Clauses")
        for i, r in enumerate(results, 1):
            st.markdown(f"**Clause {i}:** {r.page_content.strip()}")

        # Step 4: Parse query
        parsed_query = parse_query(query)

        # Step 5: Evaluate decision
        st.info("🤖 Thinking...")
        decision = evaluate_decision(parsed_query, results)

        st.subheader("✅ Final Decision")
        st.code(decision, language="json")

    except Exception as e:
        st.error(f"❌ Error: {e}")

else:
    st.caption("Please upload a PDF and enter your query to begin.")
