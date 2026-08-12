from retrieval.search import search_documents


DOCUMENTS = [
    "Day16 taught short-term memory with messages.",
    "Day17 taught RAG and similarity search.",
    "Day18 added knowledge_search as a wrapper tool.",
    "Day15 added a text_length tool.",
    "Day08 introduced Git branch and merge.",
]


def knowledge_search(query: str) -> str:
    results = search_documents(query, DOCUMENTS, top_k=1)

    if not results:
        return "No relevant knowledge found."

    score, document = results[0]

    if score == 0:
        return "No relevant knowledge found."

    return document
