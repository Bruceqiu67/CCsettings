"""天气查询工具测试."""

from __future__ import annotations

import json
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

    def test_city_weather_has_humidity(self) -> None:
        weather = CityWeather(city="北京", temperature=28.0, humidity=65.0)
        assert weather.humidity == 65.0

    def test_city_weather_humidity_default_none(self) -> None:
        """humidity 默认值为 None."""
        weather = CityWeather(city="北京", temperature=28.0)
        assert weather.humidity is None

    def test_city_weather_equality(self) -> None:
        """相同字段的两个实例相等."""
        a = CityWeather(city="北京", temperature=28.0, humidity=65.0)
        b = CityWeather(city="北京", temperature=28.0, humidity=65.0)
        assert a == b

    def test_city_weather_repr(self) -> None:
        """repr 包含城市名."""
        weather = CityWeather(city="北京", temperature=28.0)
        r = repr(weather)
        assert "北京" in r
        assert "28.0" in r


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
    def test_get_weather_valid_city(
        self, service: MockWeatherService, city: str, expected_temp: float
    ) -> None:
        weather = service.get_weather(city)
        assert weather.city == city
        assert weather.temperature == expected_temp

    def test_get_weather_invalid_city(self, service: MockWeatherService) -> None:
        with pytest.raises(ValueError, match="不支持的城市"):
            service.get_weather("广州")

    @pytest.mark.parametrize(
        ("city", "expected_humidity"),
        [
            ("北京", 65.0),
            ("上海", 78.0),
            ("深圳", 82.0),
        ],
    )
    def test_get_weather_returns_humidity(
        self, service: MockWeatherService, city: str, expected_humidity: float
    ) -> None:
        weather = service.get_weather(city)
        assert weather.humidity == expected_humidity

    def test_get_weather_error_message_contains_city(
        self, service: MockWeatherService
    ) -> None:
        """错误信息应包含不支持的城市的名称."""
        with pytest.raises(ValueError, match="广州") as exc_info:
            service.get_weather("广州")
        assert "不支持的城市" in str(exc_info.value)

    def test_get_weather_supported_cities_three(self, service: MockWeatherService) -> None:
        """支持恰好三个城市."""
        for city in ("北京", "上海", "深圳"):
            weather = service.get_weather(city)
            assert isinstance(weather, CityWeather)


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

    def test_cli_humidity_flag(self, capsys: pytest.CaptureFixture[str]) -> None:
        exit_code = main(["--humidity", "北京"])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert "北京: 65.0%" in captured.out

    def test_cli_json_flag(self, capsys: pytest.CaptureFixture[str]) -> None:
        exit_code = main(["--json", "北京"])
        captured = capsys.readouterr()
        assert exit_code == 0
        data = json.loads(captured.out)
        assert data["city"] == "北京"
        assert data["temperature"] == 28.0
        assert data["humidity"] == 65.0

    def test_cli_json_without_humidity_data(self, capsys: pytest.CaptureFixture[str]) -> None:
        """模拟 humidity=None 时 JSON 输出含有 null."""
        exit_code = main(["--json", "北京"])
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert "humidity" in data
        assert data["humidity"] == 65.0

    def test_cli_humidity_shows_na_when_none(self, capsys: pytest.CaptureFixture[str]) -> None:
        """humidity 为 None 时显示 N/A."""
        # Build a CityWeather with humidity=None and monkey-patch the service
        from weather_cli.cli import MockWeatherService
        original_service = MockWeatherService

        class _NoHumidityService(MockWeatherService):
            _DATA = {"北京": {"temperature": 28.0, "humidity": None}}

        # Temporarily replace the service class
        import weather_cli.cli as cli_mod
        cli_mod.MockWeatherService = _NoHumidityService
        try:
            exit_code = main(["--humidity", "北京"])
        finally:
            cli_mod.MockWeatherService = original_service

        captured = capsys.readouterr()
        assert exit_code == 0
        assert "N/A" in captured.out
