---
name: "source-command-code-check"
description: "启动代码审查流程——检查当前分支的变更质量"
---

# source-command-code-check

Use this skill when the user asks to run the migrated source command `code-check`.

## Command Template

# Code Check Command

审查当前分支的未提交变更，确保代码质量。

## 执行合约（不可违反）

- **禁止**：修改任何文件（只审查不修改）
- **必须**：先看 `git diff` 了解变更范围
- **必须**：输出结构化审查报告

## 审查流程

### Step 1: 查看变更
运行 `git diff` 了解变更的文件和内容。

### Step 2: 智能体审查
使用 Agent 工具调用 `reviewer` agent 进行深度审查：
- subagent_type: reviewer
- prompt: 审查当前 git diff 的变更

### Step 3: 输出报告
汇总审查结果，按严重程度排序输出给用户。
