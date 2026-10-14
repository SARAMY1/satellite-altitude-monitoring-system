"""Tests for the beginner satellite altitude monitoring project."""
import unittest
from satellite_altitude_monitor import (
    ALTITUDES, average_altitude, classify_altitude, count_warnings,
    altitude_extremes, altitude_deviation, build_report
)


class AltitudeMonitorTests(unittest.TestCase):
    def test_average(self):
        self.assertAlmostEqual(average_altitude(ALTITUDES), 399.5714285714)

    def test_classifications(self):
        self.assertEqual(classify_altitude(387), "LOW")
        self.assertEqual(classify_altitude(411), "HIGH")
        self.assertEqual(classify_altitude(390), "NORMAL")
        self.assertEqual(classify_altitude(410), "NORMAL")

    def test_warning_count(self):
        self.assertEqual(count_warnings(ALTITUDES), 1)

    def test_extremes(self):
        self.assertEqual(altitude_extremes(ALTITUDES), (387, 410))

    def test_deviation(self):
        self.assertEqual(altitude_deviation([405, 387]), [5, -13])

    def test_report(self):
        self.assertIn("399.57 km", build_report(ALTITUDES))
        self.assertIn("ATTENTION REQUIRED", build_report(ALTITUDES))

    def test_empty_average(self):
        with self.assertRaises(ValueError):
            average_altitude([])


if __name__ == "__main__":
    unittest.main()
