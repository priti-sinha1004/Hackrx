import re
from transformers import pipeline

ner = pipeline("ner", model="dslim/bert-base-NER")

def parse_query(text):
    entities = ner(text)

    extracted = {
        "age": None,
        "procedure": None,
        "location": None,
        "policy_duration": None
    }

    # Extract age with regex
    age_match = re.search(r"\b([1-9][0-9])\b", text)
    if age_match:
        extracted["age"] = int(age_match.group(1))

    # Extract procedure (basic examples)
    procedures = ["knee surgery", "heart surgery", "ACL surgery", "bypass", "angioplasty"]
    for proc in procedures:
        if proc in text.lower():
            extracted["procedure"] = proc
            break

    # Extract location from NER
    for ent in entities:
        if ent["entity"] == "B-LOC":
            extracted["location"] = ent["word"]
            break
    return extracted  # <- Ensure this is present at the end
