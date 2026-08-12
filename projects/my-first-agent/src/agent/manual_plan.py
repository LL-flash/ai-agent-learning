from tools.knowledge_search import knowledge_search


def run_manual_plan() -> list[str]:
    plan = [
        "Day16 memory messages",
        "Day17 RAG similarity search",
        "Day18 knowledge_search wrapper",
    ]

    observations = []

    for step in plan:
        result = knowledge_search(step)
        observations.append(result)

    return observations


def summarize_observations(observations: list[str]) -> str:
    return "\n".join(observations)


if __name__ == "__main__":
    observations = run_manual_plan()
    summary = summarize_observations(observations)
    print(summary)
