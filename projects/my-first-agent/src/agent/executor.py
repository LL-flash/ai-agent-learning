from tools.registry import TOOLS


class Executor:
    def run(self, plan):
        if plan["action"] == "chat":
            return plan["input"]

        tool_name = plan["tool"]

        if tool_name not in TOOLS:
            return f"Tool not found: {tool_name}"

        tool_func = TOOLS[tool_name]

        if tool_name == "weather":
            return tool_func(plan["city"])

        if tool_name == "calculator":
            return tool_func(plan["expression"])

        return f"Unknown tool: {tool_name}"