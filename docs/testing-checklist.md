# 测试审查清单

每次修改后按这个清单逐层验证，避免表面测试漏掉问题。

---

## 层级 1：语法检查（最表层）

```
□ JSON/YAML 格式正确
□ 文件存在且路径正确
□ 配置项名称拼写正确
```

## 层级 2：单元验证（能跑吗）

```
□ CLI 命令能正常执行（npx --help）
□ API 能正常响应（MCP initialize 握手）
□ Python 测试全部通过（pytest）
```

## 层级 3：集成验证（Claude Code 实际能识别吗）

```
□ 进 claude 跑 /xxx 命令能出来
□ 进 claude 跑 /mcp 能看到服务
□ 进 claude 跑 /skills 能看到技能
□ /agents 能看到智能体
```

## 层级 4：端到端验证（真的能用吗）

```
□ Playwright: "打开 baidu.com 截图保存"
□ Context7: "@context7 查 pytest tmp_path 用法"
□ dev-plan: "/dev-plan 写个 Hello World"
□ code-check: "/code-check 审查当前 diff"
```

## 层级 5：跨项目验证（全局配置生效吗）

```
□ 在 CCproject 目录外新建文件夹
□ 进 claude
□ /mcp 能看到全局 MCP 服务
□ /skills 能看到全局技能
□ 全局 hooks 有提示音
```

---

## 历史教训（避免重复踩坑）

| 日期 | 问题 | 根因 | 本应怎么测 |
|------|------|------|-----------|
| 2026-06-26 | MCP 包名错误 | 想当然用了 @anthropic-ai 前缀 | 应该先 `npm view` 确认包存在 |
| 2026-06-26 | computer-use 保留名 | 不知道系统占用 | 应该先进 claude 看报错信息 |
| 2026-06-26 | 全局 MCP 不生效 | 把配置写到了 settings.json 而不是 ~/.claude.json | 应该先查文档确认全局 MCP 配置位置 |
| 2026-06-26 | chrome-devtools 连不上 | 没意识到需要 Chrome 浏览器 | 应该先看包的文档/help |

## 原则

1. **先复现问题 → 再修 → 再验证问题消失**
2. **别假设配置位置，先查文档确认**
3. **最终验证要在 claude 里实际跑一次，不是只看文件和代码**
4. **修完一个地方，检查是否有其他地方也需要同步改**
