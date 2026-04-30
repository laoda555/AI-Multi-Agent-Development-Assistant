 AI Multi-Agent Development Assistant

 项目简介

本项目是一个面向开发者与课程实验场景的多 Agent 自动化系统，
用于完成代码生成、调试修复与实验报告自动生成。

 核心功能

 自动任务拆解（Planner Agent）
 代码生成与优化（Code Agent）
 错误定位与修复（Debug Agent）
 实验报告生成（Report Agent）
 上下文记忆（Memory / RAG）

 系统架构

系统采用多 Agent 协作架构：

 Planner 负责任务规划
 多 Agent 并发执行
 支持长上下文推理（20k~100k tokens）

 应用场景

 工程数学实验自动生成
 Spark 数据处理实验
 Python 项目调试
 自动化报告生成

 Token 消耗情况（测试阶段）

 单任务：20k ~ 80k tokens
 日均预计：30M ~ 100M tokens

 项目状态

当前处于开发与测试阶段，持续优化中。
## Quick Start

```bash
python main.py
