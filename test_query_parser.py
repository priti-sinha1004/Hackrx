from query_parser import parse_query

query = "My dad, 52, had a knee surgery in Pune 2 months ago. Can we claim?"
result = parse_query(query)

print("[RESULT]", result)
