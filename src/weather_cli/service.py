"""天气服务层."""

from __future__ import annotations

from abc import ABC, abstractmethod

from weather_cli.models import CityWeather, CityWeatherDict


class WeatherService(ABC):
    """天气服务抽象基类."""

    @abstractmethod
    def get_weather(self, city: str) -> CityWeather:
        """获取指定城市的天气数据."""


class MockWeatherService(WeatherService):
    """模拟天气服务，内置三个城市的固定天气数据."""

    _DATA: dict[str, CityWeatherDict] = {
        "北京": {"temperature": 28.0, "humidity": 65.0},
        "上海": {"temperature": 30.0, "humidity": 78.0},
        "深圳": {"temperature": 32.0, "humidity": 82.0},
    }

    def get_weather(self, city: str) -> CityWeather:
        """返回模拟天气数据（温度+湿度）."""
        if city not in self._DATA:
            msg = f"不支持的城市: {city}，可用城市: {', '.join(self._DATA)}"
            raise ValueError(msg)
        data = self._DATA[city]
        return CityWeather(
            city=city,
            temperature=data["temperature"],
            humidity=data["humidity"],
        )
