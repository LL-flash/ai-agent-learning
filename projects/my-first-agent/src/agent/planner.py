from tools.registry import TOOLS_SCHEMA

def plan(task):

    if "weather" in task:
        city = task.split()[-1]

        return {
            "action": "use_tool",
            "tool": "weather",
            "city": city,
        }

    if any(operator in task for operator in ["+", "-", "*", "/"]):
        return {
            "action": "use_tool",
            "tool": "calculator",
            "expression": task,
        }

    return {
        "action": "chat",
        "input": task,
    }