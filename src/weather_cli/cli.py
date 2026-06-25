"""命令行入口."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict

from weather_cli.service import MockWeatherService


def create_parser() -> argparse.ArgumentParser:
    """构建命令行参数解析器."""
    parser = argparse.ArgumentParser(
        description="天气查询工具 — 查询城市当前温度",
        epilog="示例: weather 北京",
    )
    parser.add_argument("city", help="城市名称（北京 / 上海 / 深圳）")

    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument(
        "--humidity", action="store_true", help="查询湿度"
    )
    output_group.add_argument(
        "--json", action="store_true", help="以 JSON 格式输出"
    )
    return parser


def main(argv: list[str | None] | None = None) -> int:
    """CLI 主入口，返回退出码."""
    parser = create_parser()
    args = parser.parse_args(argv)

    service = MockWeatherService()
    try:
        weather = service.get_weather(args.city)
    except ValueError as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1

    if args.json:
        data = asdict(weather)
        print(json.dumps(data, ensure_ascii=False, default=str))
    elif args.humidity:
        humid = f"{weather.humidity}%" if weather.humidity is not None else "N/A"
        print(f"{weather.city}: {humid}")
    else:
        print(f"{weather.city}: {weather.temperature}°C")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
