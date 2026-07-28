from llm.client import LLMClient
from agent.executor import Executor


llm = LLMClient()
executor = Executor()

while True:

    task = input("\nUser: ")

    if task == "exit":
        break


    try:

        plan = llm.chat(task)

        print("\nPlan:")
        print(plan)


        result = executor.run(plan)

        print("\nAgent:")
        print(result)


    except Exception as e:

        print("\nError:")
        print(e)