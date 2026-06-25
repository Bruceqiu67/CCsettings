"""天气数据模型."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


@dataclass(frozen=True)
class CityWeather:
    """城市天气信息."""

    city: str
    temperature: float
    humidity: float | None = None


class CityWeatherDict(TypedDict):
    """城市天气原始数据（服务层内部用）. """

    temperature: float
    humidity: float
