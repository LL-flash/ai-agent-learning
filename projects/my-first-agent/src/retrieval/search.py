import math
import string

VOCABULARY = [
    "memory",
    "messages",
    "tool",
    "text",
    "git",
    "branch",
    "merge",
    "rag",
    "similarity",
    "search",
    "knowledge_search",
    "wrapper",
]


def vectorize(text):
    words = [
        word.strip(string.punctuation)
        for word in text.lower().split()
    ]

    return [
        1 if word in words else 0
        for word in VOCABULARY
    ]


def dot_product(first_vector, second_vector):
    return sum(
        first * second
        for first, second in zip(first_vector, second_vector)
    )


def vector_length(vector):
    return math.sqrt(
        sum(value * value for value in vector)
    )


def cosine_similarity(first_vector, second_vector):
    first_length = vector_length(first_vector)
    second_length = vector_length(second_vector)

    if first_length == 0 or second_length == 0:
        return 0

    return dot_product(first_vector, second_vector) / (
        first_length * second_length
    )


def search_documents(query, documents, top_k=1):
    results = []
    query_vector = vectorize(query)

    for document in documents:
        document_vector = vectorize(document)
        score = cosine_similarity(query_vector, document_vector)
        results.append((score, document))

    return sorted(
        results,
        key=lambda item: item[0],
        reverse=True,
    )[:top_k]
