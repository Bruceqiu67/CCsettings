---
name: python-style
description: 应用 Python 代码风格规范
user-invocable: false
---
## Python 风格规范

- 使用 Ruff 进行格式化和 lint
- 行长度 88 字符（Black 标准）
- 使用 `ruff check --fix` 自动修复问题
- 使用 `ruff format` 格式化代码
- 所有函数和方法的参数必须有类型注解
- 返回值也必须有类型注解
- 使用 `pathlib` 而不是 `os.path`
- 异常处理要具体，不要裸 `except:`
- 日志使用 `loguru` 或标准库 `logging`
- 配置使用 Pydantic Settings
- 异步代码使用 `asyncio`
