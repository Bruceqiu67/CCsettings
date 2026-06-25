"""天气查询工具测试."""

from __future__ import annotations

import pytest

from weather_cli.models import CityWeather
from weather_cli.service import MockWeatherService
from weather_cli.cli import main


class TestCityWeather:
    """CityWeather 模型测试."""

    def test_city_weather_fields(self) -> None:
        weather = CityWeather(city="北京", temperature=28.0)
        assert weather.city == "北京"
        assert weather.temperature == 28.0

    def test_city_weather_is_frozen(self) -> None:
        weather = CityWeather(city="北京", temperature=28.0)
        with pytest.raises(AttributeError):
            weather.city = "上海"  # type: ignore[misc]


class TestMockWeatherService:
    """MockWeatherService 测试."""

    @pytest.fixture
    def service(self) -> MockWeatherService:
        return MockWeatherService()

    @pytest.mark.parametrize(
        ("city", "expected_temp"),
        [
            ("北京", 28.0),
            ("上海", 30.0),
            ("深圳", 32.0),
        ],
    )
    def test_get_temperature_valid_city(
        self, service: MockWeatherService, city: str, expected_temp: float
    ) -> None:
        weather = service.get_temperature(city)
        assert weather.city == city
        assert weather.temperature == expected_temp

    def test_get_temperature_invalid_city(self, service: MockWeatherService) -> None:
        with pytest.raises(ValueError, match="不支持的城市"):
            service.get_temperature("广州")


class TestCli:
    """CLI 入口测试."""

    def test_cli_valid_city(self, capsys: pytest.CaptureFixture[str]) -> None:
        exit_code = main(["北京"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert "北京: 28.0°C" in captured.out

    def test_cli_invalid_city(self, capsys: pytest.CaptureFixture[str]) -> None:
        exit_code = main(["广州"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "错误" in captured.err
        assert "不支持的城市" in captured.err
