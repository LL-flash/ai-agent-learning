from agent.executor import Executor
from llm.client import LLMClient
from tools.registry import TOOLS_SCHEMA


MAX_TOOL_ROUNDS = 5
MAX_MESSAGES = 10

executor = Executor()
llm = LLMClient()

messages = []


def trim_messages(messages: list[dict], max_messages: int) -> list[dict]:
    recent_messages = messages[-max_messages:]

    while recent_messages and recent_messages[0].get("role") != "user":
        recent_messages.pop(0)

    return recent_messages


while True:
    task = input("\nUser: ")

    if task == "exit":
        break

    messages.append(
        {
            "role": "user",
            "content": task,
        }
    )

    try:
        assistant_message = llm.create_message(
            messages,
            tools=TOOLS_SCHEMA,
        )

        tool_round = 0

        while assistant_message.tool_calls:
            tool_round += 1

            if tool_round > MAX_TOOL_ROUNDS:
                print("\nError:")
                print("Too many tool rounds")
                break

            pending_messages = [
                assistant_message.model_dump(exclude_none=True)
            ]

            tool_failed = False
            error_result = ""

            for tool_call in assistant_message.tool_calls:
                print("\nTool call:")
                print(tool_call.function.name)
                print(tool_call.function.arguments)

                result = executor.run_tool_call(tool_call)

                if result.startswith("Error:"):
                    tool_failed = True
                    error_result = result
                    break

                pending_messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result,
                    }
                )

                print("\nTool result:")
                print(result)

            if tool_failed:
                messages.append(
                    {
                        "role": "assistant",
                        "content": f"Tool execution failed: {error_result}",
                    }
                )
                print("\nError:")
                print(error_result)
                messages = trim_messages(messages, MAX_MESSAGES)
                break

            messages.extend(pending_messages)

            assistant_message = llm.create_message(
                messages,
                tools=TOOLS_SCHEMA,
            )

        else:
            print("\nAgent:")
            print(assistant_message.content)

            messages.append(
                {
                    "role": "assistant",
                    "content": assistant_message.content,
                }
            )

            messages = trim_messages(messages, MAX_MESSAGES)

            continue

    except Exception as e:
        print("\nError:")
        print(e)
