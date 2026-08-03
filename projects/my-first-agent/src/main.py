from agent.executor import Executor
from llm.client import LLMClient
from tools.registry import TOOLS_SCHEMA


executor = Executor()
llm = LLMClient()

while True:
    task = input("\nUser: ")

    if task == "exit":
        break

    try:
        messages = [
            {"role": "user", "content": task},
        ]

        assistant_message = llm.create_message(
            messages,
            tools=TOOLS_SCHEMA,
        )

        if assistant_message.tool_calls:
            tool_call = assistant_message.tool_calls[0]

            print("\nTool call:")
            print(tool_call.function.name)
            print(tool_call.function.arguments)

            result = executor.run_tool_call(tool_call)

            messages.append(
                assistant_message.model_dump(exclude_none=True)
            )
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result,
                }
            )

            final_message = llm.create_message(messages)

            print("\nTool result:")
            print(result)

            print("\nAgent:")
            print(final_message.content)
        else:
            print("\nAgent:")
            print(assistant_message.content)


    except Exception as e:
        print("\nError:")
        print(e)
