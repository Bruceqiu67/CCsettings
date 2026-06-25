---
name: session-note
description: 生成当前会话的摘要和标签，方便回顾和整理
argument-hint: [optional-tag]
model: haiku
allowed-tools:
  - "Read"
  - "Grep"
---

# Session Note

为当前会话生成结构化摘要，方便日后回顾。

## 执行合约

- **禁止**：修改任何文件
- **必须**：基于当前会话历史生成内容

### Fail-closed guardrail
如果无法获取会话历史，输出错误信息并停止，不要编造内容。

## 任务

分析当前会话历史，生成：

### 1. 会话标签
根据会话内容生成 3-5 个标签，例如：
`[feature] [refactor] [backend] [api]`

### 2. 一句话总结
用一句话概括本次会话做了什么。

### 3. 变更清单
列出本次会话创建或修改的文件。

### 4. 待办事项
如果有未完成的工作或下一步建议，列出来。

## 输出格式

```
## 📋 Session: [标签]

**总结**: [一句话]

**变更**: 
- [文件名]: [变更描述]

**下一步**: [如果有的话]
```

## 使用方式

会话结束时运行 `/session-note`，将输出粘贴到你的笔记或 commit 信息中。
