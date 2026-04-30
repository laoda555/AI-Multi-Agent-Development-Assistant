# AI 多智能体开发助手（Multi-Agent Development Assistant）

## 项目简介

本项目是一个面向开发者与课程实验场景的多 Agent 自动化系统，
用于完成代码生成、错误调试与实验报告自动生成。

系统通过多 Agent 协作与链式任务执行，实现从“需求输入”到“结果输出”的自动化流程。

---

## 核心功能

* **Planner Agent**：任务拆解与流程规划
* **Code Agent**：代码生成与优化（Python / Spark）
* **Debug Agent**：错误定位与自动修复
* **Report Agent**：实验报告自动生成
* **Memory / RAG**：上下文记忆与历史任务复用

---

## 系统架构

系统采用多 Agent 协作架构，支持链式执行与上下文传递：

* 多 Agent 按阶段执行（Plan → Code → Debug → Report）
* 支持长上下文推理（20k ~ 100k tokens）
* 支持多轮任务与状态传递（Memory 模块）

---

## Workflow

User Request
↓
Planner Agent（任务拆解）
↓
Code Agent（代码生成）
↓
Debug Agent（错误修复）
↓
Report Agent（报告生成）
↓
Output

---

## 应用场景

* 工程数学实验自动生成（含计算与分析）
* Spark 数据处理实验代码生成
* Python 项目调试与优化
* 自动化实验报告生成

---

## Example

### Input

生成一个工程数学实验报告

### Output

[System] Task Started
[PlannerAgent] 拆解任务
[CodeAgent] 生成代码
[DebugAgent] 修复错误
[ReportAgent] 生成报告

实验报告：

1. 实验目的：验证自动化流程
2. 实验过程：系统自动生成代码并执行
3. 实验结果：成功
4. 实验总结：多 Agent 提升效率

---

## Token Usage（测试阶段）

* 单任务上下文：20k ~ 80k tokens
* 多 Agent 协作涉及多轮模型调用（链式推理）
* Debug 与 Report 阶段会产生额外 token 消耗
* 并发执行时预计日消耗：30M ~ 100M tokens

> 注：当前为开发测试阶段，尚未进行大规模并发压测

---

## Logs

示例运行日志见：
`logs/sample_run.txt`

日志包含：

* 多 Agent 执行流程
* Token 使用统计
* 任务执行状态

---

## Quick Start

```bash
python main.py
```

---

## Project Structure

```
ai-agent-system/
├── main.py
├── planner.py
├── coder.py
├── debugger.py
├── reporter.py
├── memory.py
├── logs/
│   └── sample_run.txt
```

---

## Roadmap

* [ ] 多 Agent 并发调度
* [ ] 长上下文（100k+ tokens）支持
* [ ] Benchmark 测试与模型对比
* [ ] Web Demo 接入

---

## 项目状态

当前处于开发与测试阶段，持续优化中。
