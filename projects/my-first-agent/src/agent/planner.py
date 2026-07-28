class Planner:

    def __init__(self):
        print("Planner initialized")


    def plan(self, task):

        if "weather" in task:

            city = task.split()[-1]

            return {
                "action": "use_tool",
                "tool": "weather",
                "city": city
            }


        return {
            "action": "chat",
            "input": task
        }