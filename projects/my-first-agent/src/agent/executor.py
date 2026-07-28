from tools.registry import tools


class Executor:


    def __init__(self):
        print("Executor initialized")


    def run(self, plan):

        if plan.get("tool"):

            tool = tools[plan["tool"]]

            return tool(plan["city"])

        return "No tool found"