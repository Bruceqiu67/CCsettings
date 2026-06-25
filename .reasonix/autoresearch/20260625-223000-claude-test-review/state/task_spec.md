# Task: Claude Code 配置实战验证与修复

## Goal
验证 CCproject 的 Claude Code 配置在 4 个实战场景中的表现，修复发现的问题。
生成一份"配置健康检查报告"。

## 测试结果摘要
1. `/dev-plan`: ✅ 完美 — 出方案→确认→coder agent→测试 全链路成功
2. `--json`: ⚠️ 完成了但 PROACTIVELY agent 没自动激活，Claude inline 改的
3. Playwright: ⚠️ 没用 MCP server，自己写 Python 脚本绕过的
4. `/code-check`: ✅ 完美 — reviewer agent 详细报告

## 待修复问题
1. --json 和 --humidity 应互斥
2. _DATA 用 TypedDict
3. get_temperature() 改名 get_weather()
4. 测试缺口
