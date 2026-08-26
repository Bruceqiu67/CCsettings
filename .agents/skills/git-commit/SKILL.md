---
name: git-commit
description: 根据代码变更生成规范的 git commit 信息
allowed-tools:
  - "Bash(git *)"
user-invocable: true
---

# Git Commit Skill

根据 git diff 生成符合 Conventional Commits 规范的提交信息。

## 任务
分析当前工作区的变更，生成提交信息。

## 指令
1. 运行 `git diff` 了解变更内容
2. 运行 `git diff --cached --stat` 了解暂存区
3. 根据变更内容生成提交信息

## 提交信息格式
```
type(scope): 简短描述（50字以内）

可选详细说明（72字换行）
```

## 类型
- `feat`: 新功能
- `fix`: 修复 Bug
- `refactor`: 重构
- `test`: 测试
- `docs`: 文档
- `chore`: 杂项
- `perf`: 性能优化

## 预期输出
```
git commit -m "type(scope): description" -m "详细说明"
```
