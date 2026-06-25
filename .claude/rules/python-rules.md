---
paths:
  - src/**/*.py
  - tests/**/*.py
---
# Python 开发规则

当你编辑 Python 文件时，遵循以下规则：

## 导入顺序
1. 标准库（os, sys, pathlib 等）
2. 第三方库（pydantic, requests 等）
3. 本地模块

每个分组之间空一行。

## 命名规范
- 类名: `CamelCase`
- 函数/方法: `snake_case`
- 常量: `UPPER_SNAKE_CASE`
- 私有: `_leading_underscore`

## 测试命名
- 测试文件: `test_<module>.py`
- 测试函数: `test_<function>_<scenario>`
- 测试类: `Test<ClassName>`
