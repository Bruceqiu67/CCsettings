"""Claude Code Hooks — Windows 版（使用 winsound 蜂鸣提示音）"""

from __future__ import annotations

import json
import os
import sys
import winsound
from pathlib import Path


def play_tone(frequency: int, duration: int) -> None:
    """播放一个指定频率和持续时间的蜂鸣音。"""
    try:
        winsound.Beep(frequency, duration)
    except Exception:
        pass  # 静默失败


def play_event_sound(hook_event: str) -> None:
    """根据 hook 事件播放对应的提示音。"""
    sounds = {
        # 会话生命周期
        "SessionStart":         (880, 150),   # 高音上升 → 启动
        "SessionEnd":           (440, 300),   # 低音下降 → 结束
        "Setup":                (660, 100),   # 中音 → 设置

        # 工具使用
        "PreToolUse":           (1200, 50),   # 短促高音 → 工具开始
        "PostToolUse":          (1000, 80),   # 中高音 → 工具完成
        "PostToolUseFailure":   (200, 400),   # 低沉嗡鸣 → 错误
        "PostToolBatch":        (1100, 60),   # 高音 → 批处理

        # 用户交互
        "UserPromptSubmit":     (900, 100),   # 提示音 → 用户发消息
        "UserPromptExpansion":  (850, 80),    # 提示音 → 扩展
        "Notification":         (1400, 80),   # 通知叮
        "MessageDisplay":       (800, 60),    # 消息显示

        # 智能体
        "SubagentStart":        (1000, 60),   # 高音 → 子智能体启动
        "SubagentStop":         (700, 100),   # 中音 → 子智能体停止
        "Stop":                 (500, 200),   # 低沉 → 终止

        # 任务
        "TaskCreated":          (960, 80),    # 新任务
        "TaskCompleted":        (1200, 120),  # 双音成功 → 任务完成

        # 压缩
        "PreCompact":           (600, 100),   # 中音 → 即将压缩
        "PostCompact":          (1000, 100),  # 恢复音 → 压缩完成

        # 权限
        "PermissionRequest":    (500, 150),   # 低沉 → 权限请求
        "PermissionDenied":     (300, 300),   # 低沉 → 拒绝

        # 其他
        "TeammateIdle":         (550, 100),   # 中低音 → 队友空闲
        "ConfigChange":         (900, 80),    # 配置变更
        "InstructionsLoaded":   (750, 80),    # 指令加载
        "Elicitation":          (650, 100),   # 澄清请求
        "ElicitationResult":    (850, 80),    # 澄清结果
        "StopFailure":          (200, 500),   # 低长音 → 终止失败
        "CwdChanged":           (700, 60),    # 目录变更
        "WorktreeCreate":       (780, 80),    # 工作树创建
        "WorktreeRemove":       (580, 100),   # 工作树移除
        "FileChanged":          (680, 60),    # 文件变更
    }

    if hook_event in sounds:
        freq, dur = sounds[hook_event]
        play_tone(freq, dur)


def main() -> None:
    """主入口：解析事件名并播放声音。"""
    # 命令行参数: --event=EventName 或直接传事件名
    args = sys.argv[1:]

    # 尝试从 USE_HOOK_EVENT 环境变量获取（某些版本使用）
    hook_event = os.environ.get("USE_HOOK_EVENT", "")

    # 从命令行参数解析
    for arg in args:
        if arg.startswith("--event="):
            hook_event = arg.split("=", 1)[1]
        elif arg.startswith("--") and "=" not in arg:
            # 跳过其它 flags
            continue
        elif not arg.startswith("--"):
            hook_event = arg

    # 如果都没找到，从 statusMessage 参数获取
    if not hook_event:
        for arg in args:
            if "statusMessage" in arg.lower() or "StatusMessage" in arg:
                parts = arg.split("=")
                if len(parts) > 1:
                    hook_event = parts[1]
                    break

    if hook_event:
        play_event_sound(hook_event)


if __name__ == "__main__":
    main()
