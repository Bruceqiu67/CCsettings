"""天气服务层."""

from __future__ import annotations

from abc import ABC, abstractmethod

from weather_cli.models import CityWeather


class WeatherService(ABC):
    """天气服务抽象基类."""

    @abstractmethod
    def get_temperature(self, city: str) -> CityWeather:
        """获取指定城市的当前温度."""


class MockWeatherService(WeatherService):
    """模拟天气服务，内置三个城市的固定温度."""

    _DATA: dict[str, float] = {
        "北京": 28.0,
        "上海": 30.0,
        "深圳": 32.0,
    }

    def get_temperature(self, city: str) -> CityWeather:
        """返回模拟温度数据."""
        if city not in self._DATA:
            msg = f"不支持的城市: {city}，可用城市: {', '.join(self._DATA)}"
            raise ValueError(msg)
        return CityWeather(city=city, temperature=self._DATA[city])
