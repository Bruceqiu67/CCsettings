# 🧊 CCsettings — Claude Code 最佳实践配置

一套开箱即用的 Claude Code 配置模板，全局安装后**任意项目**都能用。

> 基于 [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) 标准搭建

---

## 📦 包含什么

| 分类 | 内容 | 数量 |
|------|------|------|
| 🧠 **智能体** | coder · reviewer · debugger | 3 |
| 🎯 **斜杠命令** | /dev-plan · /code-check · /test · /session-note · /dev-cycle | 5 |
| 🛠️ **技能** | python-style · git-commit | 2 |
| 📋 **规则** | python-rules · git-rules · markdown-docs | 3 |
| 🔔 **提示音** | 20 个事件（SessionStart · PostToolUse · TaskCompleted 等） | 20 |
| 🌐 **MCP 服务** | Playwright · Context7 · DeepWiki · Computer Use · Chrome DevTools | 5 |
| 🤝 **Agent Teams** | 独立团队：planner → coder → reviewer | 1 套 |
| 📊 **增强** | Status Line · Spinner 动词 · Attribution · Output Style | — |
| ⚙️ **其他** | Worktree 配置 · 跨仓库访问 · 自动清理旧会话 | — |

---

## 🚀 快速开始

### 首次安装（全局配置）

```bash
# 1. 克隆本仓库
git clone https://github.com/Bruceqiu67/CCsettings.git

# 2. 复制到全局
cd CCsettings
cp -r .claude/agents ~/.claude/
cp -r .claude/commands ~/.claude/
cp -r .claude/skills ~/.claude/
cp -r .claude/hooks ~/.claude/
cp -r .claude/rules ~/.claude/

# 3. 合并 settings.json（保留你的 API 密钥到 env 字段）
```

### 安装后

```bash
# 在任意项目目录
cd your-project
claude

# 自动获得全套配置：
#   🧠 coder / reviewer / debugger — 写代码时自动激活
#   🎯 /dev-plan — 先出方案再编码
#   🎯 /code-check — 审查代码质量
#   🎯 /test — 运行测试并诊断
#   🎯 /session-note — 会话摘要和标签
#   🎯 /dev-cycle — 5 步完整开发周期（plan→code→test→review→ship）
#   🔔 蜂鸣提示音 — 每个事件不同音调
```

---

## 🎯 斜杠命令说明

| 命令 | 用途 | 说明 |
|------|------|------|
| `/dev-plan` | **开发规划** | 出方案 → 确认 → 调 coder agent 实现 |
| `/code-check` | **代码审查** | 审 git diff，调 reviewer agent 输出报告 |
| `/test` | **测试诊断** | 运行 pytest，分析失败原因 |
| `/session-note` | **会话总结** | 生成标签 + 摘要 + 变更清单 |
| `/dev-cycle` | **完整开发周期** | 5 步：plan → code → test → review → ship |

---

## 🧠 智能体说明

| 智能体 | 触发方式 | 职责 |
|--------|---------|------|
| **coder** | PROACTIVELY（自动） | 编码实现 + 编写测试 + 类型注解 |
| **reviewer** | PROACTIVELY（自动） | 审查 git diff，检查正确性/安全性/性能 |
| **debugger** | 手动（遇到 Bug 时用） | 定位根因 + 修复方案 |

---

## 🌐 MCP 服务

| 服务 | 用途 | 安装 |
|------|------|------|
| **Playwright** | 浏览器自动化 | `npx playwright install` |
| **Context7** | 实时库文档查询 | 自动 |
| **DeepWiki** | GitHub 仓库文档检索 | 自动 |
| **Computer Use** | Claude 操控电脑 | 自动 |
| **Chrome DevTools** | Chrome 浏览器集成 | 装 Chrome 扩展 |

### 全局 MCP 配置（所有项目通用）

MCP 服务默认只在项目目录（`.mcp.json`）生效。要在**任意项目**中都能用，需配置到全局：

```bash
# 编辑 ~/.claude.json，在 mcpServers 字段中添加：
# （不要覆盖已有数据）
{
  "mcpServers": {
    "playwright": {"command": "npx", "args": ["-y", "@playwright/mcp"]},
    "context7": {"command": "npx", "args": ["-y", "@upstash/context7-mcp"]},
    "deepwiki": {"command": "npx", "args": ["-y", "deepwiki-mcp"]},
    "mcp-computer-use": {"command": "npx", "args": ["-y", "@github/computer-use-mcp"]},
    "chrome-devtools": {"command": "npx", "args": ["-y", "chrome-devtools-mcp@latest"]}
  }
}
```

### MCP 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| `"computer-use" is a reserved MCP server name` | 名称被系统占用 | 改用 `mcp-computer-use` |
| `chrome-devtools ✘ failed` | 需要 Chrome 浏览器运行 | 启动 Chrome 后再进 claude，或 `claude --chrome` |
| `No MCP servers configured` | 项目目录没有 `.mcp.json` | 将 MCP 配到全局 `~/.claude.json` |
| 第一次使用弹出确认 | MCP 首次加载需授权 | 选 `2. Use this and all future MCP servers in this project` |

---

## 🔔 提示音对照表

| 时机 | 音调 | 含义 |
|------|------|------|
| 启动 Claude | 叮↑ (880Hz) | 会话开始 |
| 你发消息 | 嘟 (900Hz) | 已收到 |
| Claude 开始做事 | 滴 (1200Hz) | 工具开始调用 |
| 完成一步 | 哔 (1000Hz) | 工具完成 |
| 调子智能体 | 滴↑ (1000Hz) | subagent 启动 |
| 智能体结束 | 嘟↓ (700Hz) | subagent 停止 |
| 出错了 | 嗡— (200Hz) | 工具失败 |
| 任务完成 | 叮叮 (1200Hz) | 任务完成 |
| 退出 Claude | 嗡↓ (440Hz) | 会话结束 |

要关掉提示音：`~/.claude/settings.json` 中设 `"disableAllHooks": true`。

---

## 🔧 如何更新

```bash
cd CCsettings
git pull
cp -r .claude/agents ~/.claude/
cp -r .claude/commands ~/.claude/
cp -r .claude/skills ~/.claude/
cp -r .claude/hooks ~/.claude/
cp -r .claude/rules ~/.claude/
```

---

## 📁 目录结构

```
CCsettings/
├── CLAUDE.md              ← 仓库记忆文件
├── README.md              ← 本文件
├── .mcp.json              ← 5 个 MCP 服务
├── pyproject.toml
│
├── .claude/
│   ├── agents/            ← coder, reviewer, debugger
│   ├── commands/          ← dev-plan, code-check, test, session-note
│   │   └── workflows/     ← dev-cycle
│   ├── skills/            ← python-style, git-commit
│   ├── hooks/             ← 20 事件蜂鸣提示音
│   ├── rules/             ← python-rules, git-rules, markdown-docs
│   ├── settings.json      ← 项目级配置
│   └── agent-memory/
│
├── agent-teams/           ← 独立多智能体团队
├── .github/workflows/     ← GitHub Actions 自动跑测试
├── changelog/
└── src/ + tests/          ← 测试项目（51 个测试）
```

---

## ⚙️ 全局配置文件层级

| 级别 | 位置 | 用途 |
|------|------|------|
| 命令行参数 | `claude --model opus` | 单次覆盖 |
| 项目级 | `.claude/settings.local.json` | **git 忽略**，个人覆盖 |
| 项目级 | `.claude/settings.json` | 团队共享 |
| **全局** | **`~/.claude/settings.json`** | **所有项目通用** |

---

## 🧪 验证安装

```bash
claude

# 在 Claude 里试试这些：
/dev-plan 写一个 Hello World
/code-check
/test
/session-note
/dev-cycle 加一个新功能
```

听到不同音调了吗？配置生效了 🎵

---

## 📚 参考

- [Claude Code 官方文档](https://code.claude.com/docs)
- [Claude Code 最佳实践](https://github.com/shanraisshan/claude-code-best-practice)
- [Claude Code Hooks](https://github.com/shanraisshan/claude-code-hooks)
