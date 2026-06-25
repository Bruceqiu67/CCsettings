# CLAUDE.md — Agent Teams

这是一个独立的多智能体团队环境。通过 `/dev-flow` 命令启动 **planner → coder → reviewer** 三智能体接力开发流程。

## 使用方式
```bash
cd agent-teams && claude
/dev-flow <需求描述>
```

## 智能体
| 角色 | 职责 |
|------|------|
| planner | 需求分析 + 技术方案设计 |
| coder | 编码实现 + 测试 |
| reviewer | 代码审查 |

## 注意
- 所有文件在 `agent-teams/` 目录外创建（即回到主项目目录）
- 团队配置在 `.claude/` 下
