from transformers import pipeline

# Use local small model for generation
generator = pipeline("text-generation", model="google/flan-t5-base", max_length=512)

def evaluate_decision(parsed_query, retrieved_docs):
    # Build a context for reasoning
    context = "\n".join(doc.page_content for doc in retrieved_docs)

    prompt = f"""
Given the following user details and policy clauses, decide:

User Info:
{parsed_query}

Policy Clauses:
{context}

Answer these:
- Is the claim approved?
- What is the eligible payout amount?
- Justify your answer with clause references.

Respond in JSON format with:
- Decision
- Amount
- Justification
"""

    result = generator(prompt, max_length=512)[0]["generated_text"]

    return result
