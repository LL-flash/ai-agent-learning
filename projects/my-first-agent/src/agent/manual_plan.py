import json

from llm.client import LLMClient
from tools.knowledge_search import knowledge_search


RETRY_QUERIES = {
    "Day16": "Day16 memory messages",
    "Day17": "Day17 RAG similarity search",
    "Day18": "Day18 knowledge_search wrapper",
}


def create_plan(task: str) -> list[str]:
    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI agent planner. "
                "Return JSON only with this format: "
                '{"steps": ["search query 1", "search query 2"]}. '
                "Create short search queries for the local learning knowledge base."
            ),
        },
        {
            "role": "user",
            "content": task,
        },
    ]

    llm = LLMClient()
    response = llm.create_message(messages)
    plan_data = json.loads(response.content)

    return plan_data["steps"]


def refine_query(step: str) -> str:
    for day, retry_query in RETRY_QUERIES.items():
        if day.lower() in step.lower():
            return retry_query

    return step


def run_plan(plan: list[str]) -> list[str]:
    observations = []

    for step in plan:
        result = knowledge_search(step)

        if result == "No relevant knowledge found.":
            retry_query = refine_query(step)
            result = knowledge_search(retry_query)

        observations.append(result)

    return observations


def summarize_observations(observations: list[str]) -> str:
    return "\n".join(observations)


if __name__ == "__main__":
    task = "Summarize what I learned from Day16 to Day18."
    plan = create_plan(task)
    print("Generated plan:")
    print(plan)
    observations = run_plan(plan)
    summary = summarize_observations(observations)
    print(summary)
