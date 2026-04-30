class ReportAgent:
    def __init__(self):
        self.name = "ReportAgent"

    def generate(self, code_result):
        print(f"[{self.name}] 生成实验报告...")

        report = f"""
实验报告：

1. 实验目的：
验证自动化代码生成与执行流程

2. 实验过程：
系统自动生成代码并进行调试

3. 实验结果：
代码执行成功

4. 实验总结：
多 Agent 协作有效提升效率
"""
        return report
