# CLAUDE.md

## 项目概览

这是 CCproject 的 Claude Code 最佳实践配置项目。本项目本身托管了 Claude Code 的各项配置（智能体、命令、技能、规则），是你使用 Claude Code 的起点。

## 技术栈

- **语言**: Python 3.12+
- **包管理**: uv 或 pip
- **测试**: pytest
- **代码风格**: Ruff (格式化 + lint)
- **类型检查**: mypy

## 目录结构

```
├── src/                       # 源代码
├── tests/                     # 测试
├── .claude/
│   ├── agents/                # 🧠 智能体
│   │   ├── coder.md           ← 编码实现
│   │   ├── reviewer.md        ← 代码审查（PROACTIVELY）
│   │   └── debugger.md        ← 调试 Bug
│   ├── commands/              # 🎯 斜杠命令
│   │   ├── dev-plan.md        ← /dev-plan 开发规划
│   │   ├── code-check.md      ← /code-check 代码审查
│   │   └── test.md            ← /test 测试诊断
│   ├── skills/                # 🛠️ 技能
│   │   └── python-style/      ← Python 风格规范
│   ├── rules/                 # 📋 规则
│   │   ├── python-rules.md    ← 编辑 .py 时加载
│   │   └── git-rules.md       ← 全局加载
│   └── settings.json          ← 项目设置
└── CLAUDE.md                  ← 本文件
```

## 关键配置说明

### 智能体
- `coder`（PROACTIVELY）：编写代码和测试，预加载 python-style 技能
- `reviewer`（PROACTIVELY）：审查 git diff 变更
- `debugger`：分析并修复 Bug

### 命令
- `/dev-plan`：先输出技术方案 → 确认后再编码
- `/code-check`：审查当前分支的代码质量
- `/test`：运行 pytest 并诊断失败原因

## 开发准则

### 代码质量
- 所有新代码必须有对应的单元测试
- 提交前运行 `pytest` 确保测试通过
- 使用 Ruff 保持代码风格一致
- 所有函数签名必须有类型注解

### Git 提交
- 每个文件单独提交，不要批量提交
- 提交信息格式：`type(scope): description`

### 工作方式
- 复杂任务先用 `/dev-plan` 出方案，确认后再实现
- 代码审查用 `/code-check`
- 上下文用到约 50% 时手动 `/compact`
- 遇到模糊的需求先问清楚再做

## 调试技巧

- 使用 `/doctor` 诊断 Claude Code 自身问题
- 运行 `/usage` 查看当前会话使用量
- 如果某条指令被忽略，尝试用更明确的措辞重述

## 最佳实践来源

本项目配置参考了 [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) 仓库的标准。

- 智能体 frontmatter 使用 `allowedTools`（YAML 数组，首字母大写）
- 命令 frontmatter 使用 `allowed-tools`（kebab-case）
- 命令设 `model: haiku` 节省 token
- 优先使用内置命令（`/plan`、`/review`），自定义命令避免冲突
