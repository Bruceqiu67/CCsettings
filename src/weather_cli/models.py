"""天气数据模型."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CityWeather:
    """城市天气信息."""

    city: str
    temperature: float
