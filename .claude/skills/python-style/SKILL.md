---
name: python-style
description: 应用 Python 代码风格规范——格式化、lint、类型注解
user-invocable: false
allowed-tools:
  - "Bash(ruff *)"
  - "Bash(mypy *)"
---

# Python Style Skill

确保 Python 代码符合项目风格规范。

## 任务

对指定的 Python 文件应用格式化和 lint 检查。

## 指令

### 1. 格式化代码
```bash
ruff format <file>
```

### 2. Lint 检查并自动修复
```bash
ruff check --fix <file>
```

### 3. 类型检查
```bash
mypy <file>
```

## 规范

| 规则 | 标准 |
|------|------|
| 行长度 | 88 字符（Black 标准） |
| 引号 | 双引号 `"` |
| 导入排序 | 标准库 → 第三方 → 本地，每组空行隔开 |
| 命名 | 类: `CamelCase`，函数: `snake_case`，常量: `UPPER_SNAKE` |
| 类型注解 | 所有函数参数和返回值必须有 |

## 预期输出

```
✅ <file>: 格式化完成
✅ <file>: lint 通过
⚠️  <file>: mypy 有 X 个警告（见上方详情）
```
