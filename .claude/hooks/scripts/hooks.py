#!/usr/bin/env python3
"""Claude Code Hooks — Windows 版，从 stdin 读取事件数据后蜂鸣提示"""

from __future__ import annotations

import json
import sys
import winsound
from pathlib import Path


def play_tone(frequency: int, duration: int) -> None:
    """播放一个指定频率和持续时间的蜂鸣音。"""
    try:
        winsound.Beep(frequency, duration)
    except Exception:
        pass


def get_sound(event_name: str) -> tuple[int, int] | None:
    """根据事件名返回 (频率, 时长)。"""
    sounds = {
        "SessionStart":         (880, 150),
        "SessionEnd":           (440, 300),
        "Setup":                (660, 100),
        "PreToolUse":           (1200, 50),
        "PostToolUse":          (1000, 80),
        "PostToolUseFailure":   (200, 400),
        "PostToolBatch":        (1100, 60),
        "UserPromptSubmit":     (900, 100),
        "UserPromptExpansion":  (850, 80),
        "Notification":         (1400, 80),
        "MessageDisplay":       (800, 60),
        "SubagentStart":        (1000, 60),
        "SubagentStop":         (700, 100),
        "Stop":                 (500, 200),
        "TaskCreated":          (960, 80),
        "TaskCompleted":        (1200, 120),
        "PreCompact":           (600, 100),
        "PostCompact":          (1000, 100),
        "PermissionRequest":    (500, 150),
        "PermissionDenied":     (300, 300),
        "TeammateIdle":         (550, 100),
        "ConfigChange":         (900, 80),
        "InstructionsLoaded":   (750, 80),
        "Elicitation":          (650, 100),
        "ElicitationResult":    (850, 80),
        "StopFailure":          (200, 500),
        "CwdChanged":           (700, 60),
        "WorktreeCreate":       (780, 80),
        "WorktreeRemove":       (580, 100),
        "FileChanged":          (680, 60),
    }
    return sounds.get(event_name)


def main() -> None:
    """从 stdin 读取 Claude 传递的 JSON，提取事件名并播放提示音。"""
    try:
        stdin_content = sys.stdin.read().strip()
        if not stdin_content:
            return

        data = json.loads(stdin_content)
        event_name = data.get("hook_event_name", "")

        if not event_name:
            return

        sound = get_sound(event_name)
        if sound:
            play_tone(*sound)

    except (json.JSONDecodeError, Exception):
        pass  # 静默失败，不打断 Claude


if __name__ == "__main__":
    main()
