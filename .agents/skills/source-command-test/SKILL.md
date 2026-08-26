---
name: "source-command-test"
description: "运行测试并诊断失败原因"
---

# source-command-test

Use this skill when the user asks to run the migrated source command `test`.

## Command Template

# Test Command

运行项目的测试套件，诊断并修复失败测试。

## 执行合约（不可违反）

- **禁止**：不运行测试就直接说"可能没问题"
- **必须**：对每个失败测试分析根因
- **必须**：修复后重新运行确认

## 测试流程

### Step 1: 运行测试
```bash
pytest -v
```

### Step 2: 分析失败
对每个失败测试，分析：
- 是测试代码有问题还是业务代码有 Bug？
- 是回归问题吗？（`git log --oneline -5`）
- 是环境问题吗？（依赖变更？配置缺失？）

### Step 3: 修复验证
- 提出修复方案
- 修复后重新运行 `pytest -v`
- 确认全部通过后报告结果
