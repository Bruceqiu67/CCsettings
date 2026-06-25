# CLAUDE.md

## 项目概览

这是 CCproject — 一个 Python 项目。

## 技术栈

- **语言**: Python 3.12+
- **包管理**: uv 或 pip
- **测试**: pytest
- **代码风格**: Ruff (格式化 + lint)
- **类型检查**: mypy

## 目录结构约定

```
├── src/              # 源代码
├── tests/            # 测试
├── docs/             # 文档
├── scripts/          # 工具脚本
├── .claude/          # Claude Code 配置
│   ├── agents/       # 子智能体
│   ├── commands/     # 斜杠命令
│   ├── skills/       # 技能
│   └── rules/        # 规则
└── CLAUDE.md         # 本文件
```

## 开发准则

### 代码质量
- 所有新代码必须有对应的单元测试
- 提交前运行 `pytest` 确保测试通过
- 使用 Ruff 保持代码风格一致：`ruff check src/`
- 类型注解：所有函数签名必须有类型注解

### Git 提交
- 每个文件单独提交，不要批量提交
- 提交信息格式：`type(scope): description`
  - `feat`: 新功能
  - `fix`: 修复
  - `refactor`: 重构
  - `test`: 测试
  - `docs`: 文档
  - `chore`: 杂项

### 工作方式
- 复杂任务先用 `/plan` 出方案，确认后再实现
- 代码审查用 `/review` 命令
- 使用任务列表分步完成大型任务
- 上下文用到约 50% 时手动 `/compact`
- 子任务尽量拆到 50% 上下文内完成

## 关键说明

- 不要修改我没有确认过的文件
- 不要在不通知我的情况下运行破坏性操作
- 遇到模糊的需求先问清楚再做
