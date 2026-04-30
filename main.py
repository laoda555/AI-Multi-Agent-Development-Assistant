from planner import PlannerAgent
from coder import CodeAgent
from debugger import DebugAgent
from reporter import ReportAgent


def run_task(user_input):
    print("[System] Task Started")

    planner = PlannerAgent()
    coder = CodeAgent()
    debugger = DebugAgent()
    reporter = ReportAgent()

    tasks = planner.plan(user_input)

    code = coder.generate(tasks)
    fixed_code = debugger.fix(code)
    report = reporter.generate(fixed_code)

    print("[Output]")
    print(report)


if __name__ == "__main__":
    run_task("生成实验报告")
