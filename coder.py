class CodeAgent:
    def __init__(self):
        self.name = "CodeAgent"

    def generate(self, tasks):
        print(f"[{self.name}] 生成代码...")
        code = """
import math

def compute():
    return sum([i*i for i in range(10)])

print(compute())
"""
        return code
