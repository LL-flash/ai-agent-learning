import json

from tools.registry import TOOLS


class Executor:
    def run(self, plan):
        if not isinstance(plan, dict):
            return "Error: plan must be a dict"

        action = plan.get("action")

        if action == "chat":
            return plan.get("input", "")

        if action != "use_tool":
            return "Error: action must be use_tool"

        tool_name = plan.get("tool")

        if not tool_name:
            return "Error: missing tool"

        if tool_name not in TOOLS:
            return f"Tool not found: {tool_name}"

        parameters = plan.get("parameters", {})

        if not isinstance(parameters, dict):
            return "Error: parameters must be a dict"

        tool_func = TOOLS[tool_name]

        try:
            return tool_func(**parameters)
        except Exception as error:
            return f"Error: tool '{tool_name}' failed: {error}"

    def run_tool_call(self, tool_call):
        tool_name = tool_call.function.name
        arguments_text = tool_call.function.arguments

        try:
            arguments = json.loads(arguments_text)
        except json.JSONDecodeError as error:
            return f"Error: failed to parse tool arguments: {error}"

        plan = {
            "action": "use_tool",
            "tool": tool_name,
            "parameters": arguments,
        }

        return self.run(plan)
