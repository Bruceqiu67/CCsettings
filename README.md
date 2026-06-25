# 🧊 CCsettings — Claude Code 最佳实践配置

一套开箱即用的 Claude Code 配置模板，包含智能体、命令、技能、规则、提示音。

> 基于 [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) 标准搭建

---

## 📦 包含什么

| 分类 | 内容 | 数量 |
|------|------|------|
| 🧠 **智能体** | coder · reviewer · debugger | 3 |
| 🎯 **斜杠命令** | /dev-plan · /code-check · /test · /session-note | 4 |
| 🛠️ **技能** | python-style · git-commit | 2 |
| 📋 **规则** | python-rules · markdown-docs | 2 |
| 🔔 **提示音** | SessionStart · PostToolUse · TaskCompleted 等 20 个事件 | 20 |
| 📊 **增强** | Status Line · Spinner 动词 · Attribution · Output Style | — |

---

## 🚀 快速开始

### 首次安装（全局配置）

```bash
# 1. 克隆本仓库
git clone https://github.com/Bruceqiu67/CCsettings.git
cd CCsettings

# 2. 创建全局 Claude Code 配置目录
mkdir -p ~/.claude

# 3. 复制配置文件
cp -r .claude/agents ~/.claude/
cp -r .claude/commands ~/.claude/
cp -r .claude/skills ~/.claude/
cp -r .claude/hooks ~/.claude/
cp -r .claude/rules ~/.claude/

# 4. 合并 settings.json（保留你的 API 密钥）
#    把 .claude/settings.json 的内容合并到 ~/.claude/settings.json 中
#    不要覆盖 env 字段（里面是 API key 等敏感信息）
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
#   🔔 蜂鸣提示音 — 每个事件不同音调
```

> **提示**: 每个项目根目录下还需要一个 `CLAUDE.md` 文件来描述项目本身（技术栈、目录结构、开发规范）。这是项目级的记忆文件，全局配置不会覆盖它。

---

## 🎯 斜杠命令说明

| 命令 | 用途 | 说明 |
|------|------|------|
| `/dev-plan` | **开发规划** | 先输出技术方案 → 等你确认 → 自动调 coder agent 实现 |
| `/code-check` | **代码审查** | 审查当前 git diff，调 reviewer agent 输出结构化报告 |
| `/test` | **测试诊断** | 运行 pytest，分析失败原因，提出修复方案 |
| `/session-note` | **会话总结** | 生成标签 + 摘要 + 变更清单 |

---

## 🧠 智能体说明

| 智能体 | 触发方式 | 职责 |
|--------|---------|------|
| **coder** | PROACTIVELY（自动） | 编码实现 + 编写测试 + 类型注解 |
| **reviewer** | PROACTIVELY（自动） | 审查 git diff，检查正确性/安全性/性能 |
| **debugger** | 手动（遇到 Bug 时用） | 定位根因 + 提出修复方案 |

智能体通过 YAML frontmatter 定义，位于 `.claude/agents/*.md`。

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

要关掉提示音：在 `~/.claude/settings.json` 或项目 `.claude/settings.json` 中设置 `"disableAllHooks": true`。

---

## 🔧 如何更新

当本仓库更新时：

```bash
# 1. 拉取最新配置
cd CCsettings
git pull

# 2. 选择性更新到全局
#    覆盖全部（会覆盖你可能的本地修改）
cp -r .claude/agents ~/.claude/
cp -r .claude/commands ~/.claude/
cp -r .claude/skills ~/.claude/
cp -r .claude/hooks ~/.claude/
cp -r .claude/rules ~/.claude/

#    或者只更新你需要的某个文件
#    比如只更新 hooks 脚本
cp .claude/hooks/scripts/hooks.py ~/.claude/hooks/scripts/
```

---

## 📁 目录结构

```
CCsettings/
├── CLAUDE.md              ← 仓库记忆文件（Claude 启动时读取）
├── README.md              ← 本文件
├── .mcp.json              ← MCP 服务器配置（Playwright + Context7 + DeepWiki）
├── pyproject.toml         ← Python 项目模板
│
├── .claude/
│   ├── agents/            ← 🧠 智能体定义
│   │   ├── coder.md
│   │   ├── reviewer.md
│   │   └── debugger.md
│   ├── commands/          ← 🎯 斜杠命令
│   │   ├── dev-plan.md
│   │   ├── code-check.md
│   │   ├── test.md
│   │   └── session-note.md
│   ├── skills/            ← 🛠️ 技能
│   │   ├── python-style/
│   │   └── git-commit/
│   ├── hooks/             ← 🔔 提示音
│   │   ├── scripts/hooks.py
│   │   └── config/hooks-config.json
│   ├── rules/             ← 📋 编码规则
│   │   ├── python-rules.md
│   │   └── markdown-docs.md
│   ├── settings.json      ← ⚙️ 主配置
│   ├── .gitignore
│   └── agent-memory/      ← 智能体持久化记忆
│
├── agent-teams/           ← 🤝 独立多智能体团队
│   └── .claude/           ← 独立运行：cd agent-teams && claude
│       ├── agents/        ← planner, coder, reviewer
│       └── commands/      ← /dev-flow
│
└── src/ + tests/          ← 测试项目（天气 CLI + 文件搜索工具）
```

---

## ⚙️ 全局配置文件层级

Claude Code 的配置按优先级从高到低：

| 级别 | 位置 | 用途 |
|------|------|------|
| 命令行参数 | `claude --model opus` | 单次覆盖 |
| 项目级 | 项目目录 `.claude/settings.local.json` | **git 忽略**，个人项目覆盖 |
| 项目级 | 项目目录 `.claude/settings.json` | 团队共享，提交到 git |
| **全局** | **`~/.claude/settings.json`** | **所有项目通用** |
| hooks 本地 | `.claude/hooks/config/hooks-config.local.json` | 个人提示音偏好 |

---

## 🧪 验证安装

```bash
claude

# 在 Claude 里试试这些：
/dev-plan 写一个 Hello World
/code-check
/test
/session-note
```

听到不同音调了吗？配置生效了 🎵

---

## 📚 参考

- [Claude Code 官方文档](https://code.claude.com/docs)
- [Claude Code 最佳实践](https://github.com/shanraisshan/claude-code-best-practice)
- [Claude Code Hooks](https://github.com/shanraisshan/claude-code-hooks)
