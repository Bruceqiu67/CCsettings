# CLAUDE.md

## 项目概览

这是 CCproject — 一个 Python 项目，也是 Claude Code 最佳实践配置的载体。

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
├── agent-teams/               # 🤝 多智能体团队（独立运行）
│   └── .claude/
│       ├── agents/            ← planner, coder, reviewer
│       └── commands/          ← /dev-flow
├── .claude/
│   ├── agents/                # 🧠 智能体
│   │   ├── coder.md           ← 编码实现（PROACTIVELY）
│   │   ├── reviewer.md        ← 代码审查（PROACTIVELY）
│   │   └── debugger.md        ← 调试 Bug
│   ├── commands/              # 🎯 斜杠命令
│   │   ├── dev-plan.md        ← /dev-plan 开发规划
│   │   ├── code-check.md      ← /code-check 代码审查
│   │   ├── test.md            ← /test 测试诊断
│   │   └── session-note.md    ← /session-note 会话总结
│   ├── skills/
│   │   └── python-style/      ← Python 风格规范
│   ├── rules/
│   │   ├── python-rules.md    ← 编辑 .py 时加载
│   │   └── git-rules.md       ← 提交规则
│   └── settings.json          ← 项目设置
├── .mcp.json                  ← 🌐 Playwright 浏览器自动化
└── CLAUDE.md                  ← 本文件
```

## 关键配置

### 🧠 智能体（代理）
| 智能体 | 触发方式 | 职责 |
|--------|---------|------|
| coder | PROACTIVELY 自动 | 编码实现 + 测试 |
| reviewer | PROACTIVELY 自动 | 代码审查 |
| debugger | 手动 / 遇到错误时 | 调试分析 |

### 🎯 斜杠命令
| 命令 | 用途 |
|------|------|
| `/dev-plan` | 先输出技术方案，确认后再编码 |
| `/code-check` | 审查当前分支代码质量 |
| `/test` | 运行 pytest 并诊断失败原因 |
| `/session-note` | 生成会话摘要和标签 |

### 🤝 Agent Teams
独立运行的多智能体团队，位于 `agent-teams/` 目录：
```bash
cd agent-teams && claude
/dev-flow
```
启动 3 个智能体接力：**planner → coder → reviewer**

### 🌐 MCP 服务
- **Playwright**：浏览器自动化（安装：`npx playwright install`）

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
- 会话结束时用 `/session-note` 生成摘要

## 调试技巧
- `/doctor` — 诊断 Claude Code 自身问题
- `/usage` — 查看会话用量
- `/mcp` — 管理 MCP 服务器连接
- `/skills` — 查看已加载的技能
