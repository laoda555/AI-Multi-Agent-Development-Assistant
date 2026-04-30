class PlannerAgent:
    def __init__(self):
        self.name = "PlannerAgent"

    def plan(self, task):
        print(f"[{self.name}] 拆解任务: {task}")
        return ["code_generation", "debug", "report"]
