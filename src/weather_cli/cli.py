"""命令行入口."""

from __future__ import annotations

import argparse
import sys

from weather_cli.service import MockWeatherService


def create_parser() -> argparse.ArgumentParser:
    """构建命令行参数解析器."""
    parser = argparse.ArgumentParser(
        description="天气查询工具 — 查询城市当前温度",
        epilog="示例: weather 北京",
    )
    parser.add_argument("city", help="城市名称（北京 / 上海 / 深圳）")
    return parser


def main(argv: list[str] | None = None) -> int:
    """CLI 主入口，返回退出码."""
    parser = create_parser()
    args = parser.parse_args(argv)

    service = MockWeatherService()
    try:
        weather = service.get_temperature(args.city)
    except ValueError as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1

    print(f"{weather.city}: {weather.temperature}°C")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
