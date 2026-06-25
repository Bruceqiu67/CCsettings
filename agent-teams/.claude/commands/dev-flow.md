---
name: dev-flow
description: 启动多智能体开发流程——规划→编码→审查→测试
model: haiku
allowed-tools:
  - "AskUserQuestion"
  - "Agent"
  - "Read"
  - "Grep"
  - "Glob"
---

# Dev Flow — 多智能体协作开发

一个完整的开发流程，4 个智能体接力完成。

## 执行合约（不可违反）

- **禁止**：跳过任何一个步骤
- **禁止**：一个智能体替另一个智能体完成工作
- **必须**：上一步完成后再启动下一步
- **必须**：每步的输出传递给下一步

## 工作流

### Step 1: 需求分析 — planner
用 Agent 工具调用 `planner` 智能体：
- 分析用户需求
- 输出技术方案（架构、文件清单、分步计划）
- 等待用户确认方案

### Step 2: 编码实现 — coder
用户确认方案后，用 Agent 工具调用 `coder` 智能体：
- 根据方案实现代码
- 编写测试
- 确保代码通过 ruff + pytest

### Step 3: 代码审查 — reviewer
用 Agent 工具调用 `reviewer` 智能体：
- 审查 git diff
- 输出审查报告

### Step 4: 最终确认
汇总所有输出，报告给用户。
