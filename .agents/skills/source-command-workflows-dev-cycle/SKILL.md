---
name: "source-command-workflows-dev-cycle"
description: "完整开发周期：plan → code → test → review → ship"
---

# source-command-workflows-dev-cycle

Use this skill when the user asks to run the migrated source command `workflows-dev-cycle`.

## Command Template

# Dev Cycle — 完整开发周期工作流

5 步走完一个功能开发：规划 → 编码 → 测试 → 审查 → 提交。

## 执行合约

- **禁止**：跳过任何一个步骤
- **必须**：上一步完成后再启动下一步
- **必须**：每步输出传递给下一步

## 工作流

### Step 1: 规划 (plan)
输出技术方案：架构、文件清单、分步计划、风险点。
等待用户确认后再继续。

### Step 2: 编码 (code)
用 Agent 工具调用 `coder` 智能体实现功能。

### Step 3: 测试 (test)
运行 `pytest -v` 验证，失败则回到 Step 2。

### Step 4: 审查 (review)
用 Agent 工具调用 `reviewer` 智能体审查变更。

### Step 5: 提交 (ship)
汇总变更信息，输出提交建议给用户。
