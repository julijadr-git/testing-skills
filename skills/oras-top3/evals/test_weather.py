import importlib.util
import unittest
from pathlib import Path
from datetime import datetime, timezone

spec = importlib.util.spec_from_file_location("weather", Path(__file__).resolve().parents[1] / "scripts" / "weather.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class WeatherTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 10, 21, 18, 0, tzinfo=timezone.utc)
        self.payload = {
            "place": {"name": "Ukmergė", "countryCode": "LT"},
            "forecastTimestamps": [
                {"forecastTimeUtc": "2026-10-21 17:00:00", "airTemperature": 6, "conditionCode": "fog"},
                {"forecastTimeUtc": "2026-10-21 19:00:00", "airTemperature": 9.5, "conditionCode": "cloudy"},
                {"forecastTimeUtc": "2026-10-21 21:00:00", "airTemperature": 8, "conditionCode": "rain"},
            ],
        }

    def test_nearest_future_and_timezone(self):
        self.assertEqual(mod.interpret("Ukmergė", self.payload, self.now), ("9.5 °C", "Debesuota", "2026-10-21 22:00"))

    def test_wrong_place_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "kitai vietovei"):
            mod.interpret("Vilnius", self.payload, self.now)

    def test_missing_temperature_not_fabricated(self):
        self.payload["forecastTimestamps"][1]["airTemperature"] = None
        self.assertEqual(mod.interpret("Ukmergė", self.payload, self.now)[0], "Duomenų nėra")

    def test_no_future_data(self):
        with self.assertRaisesRegex(ValueError, "nėra būsimos"):
            mod.interpret("Ukmergė", self.payload, datetime(2026, 10, 22, tzinfo=timezone.utc))

if __name__ == "__main__":
    unittest.main()
