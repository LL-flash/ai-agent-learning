from tools.registry import TOOLS_SCHEMA
from llm.client import LLMClient

def format_tools_schema():
    lines = []

    for tool in TOOLS_SCHEMA:
        function = tool["function"]
        name = function["name"]
        description = function["description"]
        parameters = ", ".join(
            function["parameters"]["properties"].keys()
        )

        lines.append(f"- {name}: {description}. Parameters: {parameters}")

    return "\n".join(lines)

def build_system_prompt():
    tools_guide = format_tools_schema()

    return f"""You are an AI agent planner.

Your job is to decide which tool to use.

Available tools:
{tools_guide}

Rules:
1. Return JSON only, no other text.
2. If the task needs weather, return {{"action": "use_tool", "tool": "weather", "parameters": {{"city": "..."}}}}
3. If the task needs math calculation, return {{"action": "use_tool", "tool": "calculator", "parameters": {{"expression": "..."}}}}
4. If no tool matches, return {{"action": "chat", "input": "..."}}
"""

def plan(task):

    system_prompt = build_system_prompt()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": task},
    ]

    try:
        llm = LLMClient()
        llm_plan = llm.chat(messages)
        return llm_plan

    except Exception as error:
        print("LLM planner failed, using fallback planner")
        print(error)

    if "weather" in task:
        city = task.split()[-1]

        return {
            "action": "use_tool",
            "tool": "weather",
            "parameters": {
                "city": city,
            },
        }

    if any(operator in task for operator in ["+", "-", "*", "/"]):
        return {
            "action": "use_tool",
            "tool": "calculator",
            "parameters": {
                "expression": task,
            },
        }

    return {
        "action": "chat",
        "input": task,
    }
