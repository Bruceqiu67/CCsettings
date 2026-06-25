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
├── src/weather_cli/              # 🌤️ 天气 CLI
├── tests/                        # ✅ 测试
├── agent-teams/                  # 🤝 多智能体团队
│   └── .claude/                  ← cd agent-teams && claude
│       ├── agents/               ← planner / coder / reviewer
│       └── commands/             ← /dev-flow
├── .claude/                      # 🎯 主配置
│   ├── agents/                   ← coder / reviewer / debugger
│   ├── commands/                 ← /dev-plan /code-check /test /session-note
│   ├── skills/                   ← python-style
│   ├── rules/                    ← python-rules / git-rules
│   └── settings.json             ← spinner + statusline + MCP 权限
├── .mcp.json                     # 🌐 Playwright + Context7 + DeepWiki
└── CLAUDE.md
```

## 关键配置

### 🧠 智能体
| 智能体 | 触发 | 职责 |
|--------|------|------|
| coder | PROACTIVELY | 编码 + 测试 |
| reviewer | PROACTIVELY | 审查 git diff |
| debugger | 手动 | 调试分析 |

### 🎯 斜杠命令
| 命令 | 用途 |
|------|------|
| `/dev-plan` | 先出方案再编码 |
| `/code-check` | 审查代码质量 |
| `/test` | 测试诊断 |
| `/session-note` | 会话摘要和标签 |

### 🌐 MCP 服务
- **Playwright**: 浏览器自动化（`npx playwright install`）
- **Context7**: 实时库文档查询（`npm install -g @upstash/context7-mcp`）
- **DeepWiki**: GitHub 仓库文档检索

### 🤝 Agent Teams
独立团队，3 个智能体接力：
```bash
cd agent-teams && claude
/dev-flow
```

## 开发准则

- 新代码必须配单元测试
- 提交前 `pytest` 通过
- 所有函数签名有类型注解
- 每个文件单独提交

## 调试技巧
- `/doctor` — 诊断问题
- `/usage` — 查看用量
- `/mcp` — 管理 MCP
- 上下文 ~50% 时 `/compact`
