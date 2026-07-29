from agent.planner import plan
from agent.executor import Executor


executor = Executor()

while True:
    task = input("\nUser: ")

    if task == "exit":
        break

    try:
        plan_result = plan(task)

        print("\nPlan:")
        print(plan_result)

        result = executor.run(plan_result)

        print("\nAgent:")
        print(result)

    except Exception as e:
        print("\nError:")
        print(e)